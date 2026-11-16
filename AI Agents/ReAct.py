from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage  # The foundational class for all message types in LangGraph
from langchain_core.messages import ToolMessage  # Passes data back to LLM after it calls a tool such as the content and the name of the tool
from langchain_core.messages import SystemMessage  # Message for providing instructions to the LLM
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

# Annotated is a way to type hints in python in simpler terms used to provide additional context to the type of a variable without affecting the type itself
# email = Annotated[str, "This has to be a valid email format!"]

# Sequence: To automatically handle the state updates for sequences such as by adding new messages to a chat history

# Reducer Function: Rule that controls how updates from nodes are combined with the existing state. 
# It tells us how to merge new data into the current state.
# Without a reducer, updates would have replaced the existing value entirely.


load_dotenv()

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


@tool
def add(a: int, b: int):
    """This is an additon function that adds 2 numbers together."""
    return a + b

@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b

@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b

tools = [add, subtract, multiply]

model = ChatOllama(model="qwen2.5:1.5b", temperature=0.7).bind_tools(tools)

def model_call(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(
    content="You are my AI assistant. Answer queries to the best of your ability and use available tools when necessary.")
    response = model.invoke([system_prompt] + state["messages"])
    return {
        "messages": [response]
    }

def should_continue(state: AgentState) -> AgentState:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    else:
        return "continue"


graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")
graph.add_conditional_edges(
    "our_agent",
    should_continue,
    {
        "continue": "tools",
        "end": END
    }  
    )
graph.add_edge("tools", "our_agent")

agent = graph.compile()

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user, Add 4+12 and then multiply the result by 4 and then subtract 64 from that result")]}
print_stream(agent.stream(inputs, stream_mode = "values"))

