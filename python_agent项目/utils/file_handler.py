import os
import hashlib
from utils.logger_handler import logger
# 从LangChain核心模块导入Document类，用于表示文档对象
from langchain_core.documents import Document
# 从LangChain社区模块导入PDF和文本文件加载器
from langchain_community.document_loaders import PyPDFLoader,TextLoader
def get_file_md5_hex(filepath: str):#获取文件的MD5的16进制表示
    if not os.path.exists(filepath):
        logger.error(f"[md5计算]文件：{filepath}不存在")
        return
    if not os.path.isfile(filepath):
        logger.error(f"[md5计算]文件：{filepath}不是文件")
        return
    md5_obj = hashlib.md5()#创建md5对象

    chunk_size = 4096#避免文件过大，导致内存溢出
    try:
        with open(filepath, "rb") as f:#必须二进制读取
            while  chunk := f.read(chunk_size):   # 循环读取文件块，直到文件结束
                md5_obj.update(chunk)


            md5_hex = md5_obj.hexdigest()   # 获取MD5值的16进制表示
            return md5_hex
    except Exception as e:
        logger.error(f"计算文件：{filepath}md5失败,{str(e)}")
        return  None
def listdir_with_allow_type(path: str, allow_types: tuple[str]):#返回文件夹内的文件列表（允许的文件后缀）
   files=[]
   if not os.path.isdir(path):
       logger.error(f"[listdir_with_allow_type]{path}不是文件夹")
       return allow_types

   for f in os.listdir(path): # 遍历目录下的所有文件和子目录
       if f.endswith(allow_types):  # 检查文件是否以允许的后缀名结尾
           files.append(os.path.join(path,f)) # 将符合条件的文件完整路径添加到列表
   return tuple(files) # 返回符合条件的文件路径元组

def pdf_loader(filepath: str,passwd=None)-> list[ Document]:
    return PyPDFLoader(filepath,passwd).load()
# 定义加载文本文件的函数，返回Document对象列表
def txt_loader(filepath: str)-> list[ Document]:
  return TextLoader(filepath,encoding="utf-8").load() # 使用TextLoader加载文本文件，指定UTF-8编码
