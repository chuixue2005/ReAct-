import os
# 禁用 LangChain 的追踪功能，避免使用 LangSmith
os.environ["LANGSMITH_API_KEY"] = r""
#导入LangChain Hub
from langchain import hub
#从LangChain Hub中获取ReAct的提示
prompt=hub.pull("hwchase17/react")
print(prompt)

#导入OpenAI
from langchain_openai import OpenAI

api_key = ""
SERPAPI_API_KEY = r""

#选择要使用的大模型
llm=OpenAI(api_key=api_key,base_url="https://api.xty.app/v1")
#导入SerpAPIWrapper工具包
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool

#实例化SerpAPIWrapper
search=SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
#准备工具列表
tools=[
    Tool(
        name="Search",
        func=search.run,
        description="当大模型没有相关知识时，用于搜索知识"
    )
]
#导入create_react_agent功能
from langchain.agents import create_react_agent
#构造ReAct Agent
agent=create_react_agent(llm,tools,prompt)
#导入AgentExecutor
from langchain.agents import AgentExecutor
#创建Agent执行器并传入Agent和工具
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)
#调用AgentExecutor
result = agent_executor.invoke({"input": "当前Agent最新研究进展是什么？"})
print(result)