# 大数据学习问答智能体 (BigData Learning Agent)

基于 Coze 平台开发的大数据专业答疑助手，旨在通过工程手段约束大模型的不确定性，提供稳定、精准的交互体验。

## 🌟 核心功能
- **意图澄清与反问（Prompt 调优）**：针对模型容易“直接输出长篇大论”的痛点，重写 System Prompt（引入条件分支约束），使模型在用户未明确方向时，优先执行多轮反问。
- **工具节点调用（Tool Calling）**：引入自定义工具（`ask_direction`），在特定意图下强制模型调用固定话术，实现 100% 确定性的输出。

## 📁 项目结构
- `config/`：智能体底层配置（包含模型参数、结构化 Prompt）
- `src/tools/`：自定义工具节点源码（Python）
- `src/agents/`：Agent 编排逻辑
- `scripts/`：运行与启动脚本

## 🛠️ 技术栈
- **平台**：Coze (LLM Application Framework)
- **语言**：Python
- **核心能力**：Prompt Engineering, Tool Calling, LangGraph Workflow

