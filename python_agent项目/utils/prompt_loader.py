# 导入配置处理模块，用于获取prompts配置文件
from utils.config_handler import prompts_conf
from utils.path_tool import get_abs_path
# 导入日志处理模块，用于记录日志信息
from utils.logger_handler import logger
def load_system_prompts():
    try:
       system_prompt_path = get_abs_path(prompts_conf["main_prompt_path"])
    except KeyError as e:
        logger.error(f"[load_system_prompts]在yaml配置中没有main_prompt_path配置项")
        raise e
    try:
        # 以UTF-8编码读取系统提示词文件内容并返回
        return open(system_prompt_path,"r",encoding="utf-8").read()
    except Exception as e:
        # 如果读取文件过程中出现任何异常，记录错误日志并抛出异常
        logger.error(f"[load_system_prompts]解析系统提示词出错,{str(e)}")
        raise e


# 定义加载RAG总结提示词的函数
def load_rag_prompts():
    try:
         rag_prompt_path = get_abs_path(prompts_conf["rag_summarize_prompt_path"])
    except KeyError as e:
        logger.error(f"[load_rag_prompts]在yaml配置中没有rag_summarize_prompt_path配置项")
        raise e
    try:  # 以UTF-8编码读取RAG总结提示词文件内容并返回
        return open(rag_prompt_path, "r", encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_rag_prompts]解析RAG总结提示词出错,{str(e)}")
        raise e

# 定义加载报告生成提示词的函数
def load_report_prompts():
    try:
        # 从配置中获取report_prompt_path，并转换为绝对路径
       report_prompt_path=get_abs_path(prompts_conf["report_prompt_path"])
    except KeyError as e:
        # 如果配置中没有report_prompt_path键，记录错误日志并抛出异常
        logger.error(f"[load_report_prompts]在yaml配置中没有report_prompt_path配置项")
        raise e
    try:
        return open(report_prompt_path,"r",encoding="utf-8").read()
    except Exception as e:
        logger.error(f"[load_system_prompts]解析报告生成提示词出错,{str(e)}")
        raise e


if __name__ == '__main__':
    # 测试调用load_report_prompts函数并打印结果
    print(load_report_prompts())
