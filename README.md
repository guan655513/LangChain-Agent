# LangChain-Agent
# 🤖 LangChain 扫地机器人智能客服 Agent 系统

基于 **LangChain + RAG + ChromaDB + FastAPI + Streamlit** 构建的扫地机器人智能客服 Agent 系统。

项目面向扫地机器人售后咨询、故障排查和使用报告生成等场景，通过 RAG 检索增强生成、Agent 工具调用和多轮对话，实现知识问答、故障诊断、设备信息查询以及报告生成等功能。

---

## 📌 项目简介

传统客服系统通常依赖固定规则或关键词匹配，对于复杂故障、多轮咨询和设备数据查询等场景处理能力有限。

本项目基于 LangChain 构建智能客服 Agent，将：

- 大语言模型
- RAG 知识库
- 向量数据库
- Agent 工具调用
- Prompt Engineering
- FastAPI 后端接口
- Streamlit Web 页面

进行整合，使系统能够根据用户问题自动判断任务类型，并结合知识库、设备数据和自定义工具完成回答。

---

## ✨ 核心功能

### 1. 智能客服 Agent

基于 LangChain 构建客服 Agent，支持：

- 扫地机器人产品咨询
- 使用问题解答
- 故障诊断
- 维护建议
- 使用报告生成
- 多轮上下文对话

Agent 可以根据用户问题自主选择知识库检索或调用对应工具。

---

### 2. RAG 知识库问答

构建扫地机器人领域知识库，将：

- 产品说明
- 故障排查
- 日常维护
- 使用说明

等 Markdown 文档进行文本切分。

通过 **DashScope Embeddings** 将文本转换为向量，并存储到 **ChromaDB**。

用户提出问题后，系统通过语义检索获取相关知识片段，再将检索结果交给大语言模型生成最终答案。

基本流程：

```text
用户问题
   ↓
Embedding
   ↓
ChromaDB 向量检索
   ↓
获取相关知识片段
   ↓
Prompt 拼接
   ↓
LLM
   ↓
生成回答
