from abc import ABC,abstractmethod
from typing import Optional

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.embeddings import Embeddings
from langchain_community.chat_models import ChatTongyi
from langchain_core.language_models import BaseChatModel
from utils.config_handler import rag_conf

# 定义抽象基类BaseModelFactory，作为所有模型工厂的父类
class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) ->Optional[Embeddings | BaseChatModel]:
        pass




# 定义聊天模型工厂类，继承自BaseModelFactory
class ChatModelFactory(BaseModelFactory):
    def generator(self) ->Optional[BaseChatModel]:
        return ChatTongyi(model=rag_conf["chat_model_name"])

# 定义嵌入模型工厂类，继承自BaseModelFactory
class EmbeddingsFactory(BaseModelFactory):
    def generator(self) ->Optional[Embeddings | BaseChatModel]:
        return DashScopeEmbeddings(model=rag_conf["embedding_model_name"])

# 在模块级别创建聊天模型实例，供其他模块直接使用
chat_model=ChatModelFactory().generator()
# 在模块级别创建嵌入模型实例，供其他模块直接使用
embed_model = EmbeddingsFactory().generator()
