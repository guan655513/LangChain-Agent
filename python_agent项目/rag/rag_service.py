from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from model.factory import chat_model
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate

# 定义打印提示词的辅助函数，用于调试
def print_prompt(prompt):
   print("="*20)  # 打印分隔线
   print(prompt.to_string()) # 将提示词对象转换为字符串并打印
   print("="*20)
   return prompt # 返回提示词对象（保持链式调用）

# 定义RAG总结服务类，用于基于检索结果生成总结回答
class RagSummarizeService(object):
    def __init__(self):
       self.vector_store = VectorStoreService ()     # 创建向量存储服务实例，用于存储和检索文档向量
       self.retriever = self.vector_store.get_retriever()#检索
       self.prompt_text = load_rag_prompts() # 加载RAG总结提示词文本
       self.prompt_template = PromptTemplate.from_template(self.prompt_text) # 根据提示词文本创建提示词模板对象
       self.model = chat_model   # 设置聊天模型
       self.chain = self.__init__chain()

    # 私有方法：初始化处理链，将提示词、模型和输出解析器连接起来
    def __init__chain(self):
       chain = self.prompt_template |print_prompt |self.model| StrOutputParser()
       return chain

    # 定义检索文档的方法，根据查询字符串检索相关文档
    def retriever_docs(self, query: str)-> list[Document]:
       return self.retriever.invoke(query) # 调用检索器的invoke方法，返回与查询相关的文档列表
    def rag_summarize(self, query: str)-> str:
       context_docs=self.retriever_docs(query)#参考资料文档
       context =""
       counter = 0
       for doc in context_docs:
          counter += 1
          context += f"【参考资料{counter}】:参考资料:{doc.page_content}|参考元数据:{doc.metadata}\n"
       return self.chain.invoke(
           {
               "input": query,
                "context": context,
           }
       )
if __name__ == '__main__':
    rag = RagSummarizeService()
    print(rag.rag_summarize("小户型适合那些扫地机器人"))







