import json
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, AIMessage, HumanMessage, ToolMessage, SystemMessage
from langgraph.graph import add_messages, StateGraph, START, END
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities import PythonREPL
from langchain_ollama import ChatOllama

repl = PythonREPL()
@tool
def python_repl(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Code output: {result}"
    return result_str

llmOllama = ChatOllama(
    model="llama3.2",
    base_url="http://host.docker.internal:11434",
    temperature=0,
)

research_agent = create_react_agent(
    llmOllama,
    tools=[DuckDuckGoSearchRun()],
    state_modifier="You are best at researching a topic. You should do a thorough research on the given topic, in a way so that a writing agent can take the information you gave and write a summary about it."
)

writer_agent = create_react_agent(
    llmOllama,
    tools=[DuckDuckGoSearchRun()],
    state_modifier="You are a writer that summarizes information that a research agent gives you.Your goals are the following:Write a 3 paragraph summary of the research presented to you in a formal English, as in research papers1st paragraph: An introduction and synopsis of the research, 2nd Paragraph: the main findings and explanantions, 3rd paragraph: closing the summary in a proper way."
)

class GraphState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

graph_builder = StateGraph(GraphState)
graph_builder.add_node("research_node", research_agent)
graph_builder.add_node("writer_node", writer_agent)
graph_builder.add_edge(START, "research_node")
graph_builder.add_edge("research_node", "writer_node")
graph_builder.add_edge("writer_node", END)
graph = graph_builder.compile()







