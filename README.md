# Agent-0: 多代理链式推理系统

## 项目描述

Agent-0是一个概念验证项目，旨在模拟OpenAI的O1模型的推理能力。该系统使用顺序代理方法，通过链式思考和反思技术来提出和迭代改进编码相关问题的解决方案。

本项目使用OpenAI API（推荐GPT-4模型）来驱动代理系统。每个代理都有特定的角色和目标，共同协作以产生高质量的解决方案。

## 主要特点

- 多代理系统：使用4个专门的代理进行顺序处理
- 链式思考：每个代理使用详细的推理步骤
- 迭代改进：代理们相互建立在彼此的解决方案之上
- OpenAI API集成：利用强大的语言模型能力
- 灵活的问题解决：适用于各种编码相关查询

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/agent-0.git
   cd agent-0
   ```

2. 创建并激活虚拟环境（推荐使用conda）：
   ```
   conda create -n agent-0 python=3.10
   conda activate agent-0
   ```

3. 安装依赖：
   ```
   pip install openai
   ```

## 使用方法

1. 设置环境变量：
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

2. 运行主脚本：
   ```
   python main.py
   ```

3. 根据提示输入您的问题或查询。


## 主要组件

1. Agent类（agents/agent.py）：
   - 实现单个代理的逻辑
   - 处理与OpenAI API的交互
   - 管理推理步骤和解决方案生成

2. AgentFactory类（agents/agent_factory.py）：
   - 创建和配置代理实例
   - 定义每个代理的角色和提示

3. 主脚本（main.py）：
   - 协调整个系统的流程
   - 管理用户输入和结果输出

4. 辅助功能：
   - result_formatter.py：格式化最终输出
   - user_input_handler.py：处理用户输入

## 工作流程

1. 用户输入问题或查询。
2. Agent1分析问题并提供初始解决方案。
3. Agent2审查并改进Agent1的解决方案。
4. Agent3进一步优化和扩展解决方案。
5. Agent4进行最终审查，并提供综合解决方案。
6. 系统输出格式化的最终结果。

## 自定义和扩展

您可以通过修改agents/agent_factory.py文件中的代理提示来自定义每个代理的行为和专长。此外，您还可以添加新的代理或修改现有的工作流程以适应特定需求。

## 注意事项

- 这是一个早期版本，可能在某些情况下会失败。
- 该系统最适合可以通过编码解决的问题。
- 请确保您有足够的OpenAI API配额，因为该系统可能会进行多次API调用。
- 代理的性能很大程度上取决于所使用的OpenAI模型。GPT-4通常会产生最佳结果。

## 故障排除

如果遇到问题：
1. 确保您的OpenAI API密钥有效且正确设置。
2. 检查网络连接，确保可以访问OpenAI API。
3. 查看控制台输出以获取详细的错误信息。

