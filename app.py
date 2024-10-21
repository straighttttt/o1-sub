import openai
from openai import OpenAI

import os

os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'

openai.api_key = os.getenv("OPENAI_API_KEY")  # 或者直接在代码中设置 API 密钥

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": """Response Format:

Respond in JSON format with the following keys:

- `"title"`: A brief title for the reasoning step.
- `"content"`: Detailed explanation of the reasoning step.
- `"next_action"`: `"continue"` to proceed with more steps or `"final_answer"` if you are confident in your solution.

**Example Response:**

```json
{
    "title": "Applying Advanced Concepts",
    "content": "To enhance the solution, I will...",
    "next_action": "continue"
}```"""
        }
    ]
)

print(completion.choices[0].message.content)
