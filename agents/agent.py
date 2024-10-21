# agents/agent.py

import logging
import os
import openai
from openai import OpenAI
import re
import json
import time

logger = logging.getLogger(__name__)

class Agent:
    def __init__(self, name, role_prompt):
        self.name = name
        self.role_prompt = role_prompt

    def get_solution(self, problem, previous_solution=None):
        messages = []

        # System prompt
        messages.append({"role": "system", "content": self.role_prompt})

        # User prompt
        if previous_solution:
            messages.append({"role": "user", "content": f"Problem:\n{problem}\n\nPrevious Solution:\n{previous_solution}\n\nPlease proceed with your analysis."})
        else:
            messages.append({"role": "user", "content": f"Problem:\n{problem}\n\nPlease provide your solution."})

        # Assistant initial acknowledgment
        messages.append({"role": "assistant", "content": "Understood. I will begin my reasoning steps now."})

        steps = []
        step_count = 1

        while True:
            # Build the prompt for the current reasoning step
            prompt = self.build_prompt(messages)

            try:
                response_text = self.make_api_call(prompt)
                print(response_text)
                if not response_text:
                    logger.error(f"{self.name} did not return a valid response.")
                    break
                
                # 直接将response_text添加到steps中
                steps.append((f"Step {step_count}", response_text))

                messages.append({"role": "assistant", "content": response_text})

                # 检查是否是最终答案
                if "final_answer" in response_text.lower():
                    break

                print(step_count)

                step_count += 1

            except Exception as e:
                logger.error(f"Unexpected error in {self.name}: {str(e)}")
                break

        # Compile the agent's solution
        agent_solution = self.compile_solution(steps)
        logger.info(f"{self.name} completed their solution with steps: {steps}")
        return agent_solution

    def build_prompt(self, messages):
        # Combine messages into a single prompt
        prompt = ''
        for message in messages:
            role = message['role']
            content = message['content']
            if role == 'system':
                prompt += f"System: {content}\n\n"
            elif role == 'user':
                prompt += f"User: {content}\n\n"
            elif role == 'assistant':
                prompt += f"Assistant: {content}\n\n"
        return prompt

    def make_api_call(self, prompt):
        # 配置 API 密钥
        openai.api_key = os.getenv("OPENAI_API_KEY")  # 请确保在环境变量中设置 OPENAI_API_KEY
        os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
        try:
            # 调用 OpenAI 的 ChatCompletion API 来生成响应
            client = OpenAI()
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # 选择要使用的模型，可以是 "gpt-3.5-turbo" 或 "gpt-4"
                messages=[
                    {"role": "system", "content": self.role_prompt},  # 系统角色的提示
                    {"role": "user", "content": prompt}  # 用户的问题或推理内容
                ],
                max_tokens=1500,  # 可根据需要设置响应内容的长度
                temperature=0.7, # 控制生成内容的随机性
                timeout=30 
            )

            # 提取返回的文本内容
            response_text = response.choices[0].message.content
            
            return response_text

        except Exception as e:
            logger.error(f"Error during API call for {self.name}: {str(e)}")
            return ""


    def compile_solution(self, steps):
        solution_text = ""
        for title, content in steps:
            solution_text += f"### {title}\n{content}\n\n"
        return solution_text
