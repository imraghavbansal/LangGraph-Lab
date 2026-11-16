from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]
    
llm = ChatOllama(model="qwen2.5:1.5b", temperature=0.7)

def process(state: AgentState) -> AgentState:
    """This node will solve the request you input and return the answer."""
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    print("CURRENT STATE: ", state["messages"])

    return state

graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

conversation_history = [] 

user_input = input("Enter something: ")
while user_input != "exit":
   conversation_history.append(HumanMessage(content=user_input))
   result = agent.invoke({"messages": conversation_history})
   conversation_history = result["messages"]
   user_input = input("Enter something: ")


with open("logging.txt", "w") as file:
    file.write("Your conversation Log:\n")
    
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n")
    file.write("End of conversation")
print("\nConversation Log saved to logging.txt")