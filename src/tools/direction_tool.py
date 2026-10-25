from langchain.tools import tool

_FIXED_QUESTION = (
    "请问你是想了解底层的大数据组件（如 Hadoop/Spark），"
    "还是上层的 SQL/Python 数据分析呢？请选一个，我再为你详细展开。"
)


@tool
def ask_direction() -> str:
    """当用户提问没有明确指定具体学习方向（如 Hadoop、Spark、SQL、Python 等技术）时，
    调用本工具获取固定话术，用来反问用户选择方向。返回的字符串必须一字不差地作为回答输出。"""
    return _FIXED_QUESTION