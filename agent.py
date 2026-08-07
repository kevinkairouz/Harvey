from langchain.messages import HumanMessage 
from langchain.chat_models import init_chat_model 
from schema import HarveyState 
from langchain.tools import tool 
from langgraph.prebuilt import ToolNode  
from langgraph.graph import START, END, StateGraph


 
prompt = "You are a helpful assistant named Harvey, (your name is Harvey) and you will help write code for us and debug our code"
def startAgent(state: HarveyState) -> HarveyState: 
    #future: insert into sqlite db 
    sysReponse = model.invoke(prompt) 
    harveyResponse = model.invoke(state["userQuery"]) 
    state["harvey_response"].append(harveyResponse) 
    return state 

@tool 
def createFile(filename: str) -> str: 
    """Creates file with correct extension """
    with open(filename, "x") as file: 
        pass 
    return f"Successfully made file {filename}"

allTools = [createFile]
model = init_chat_model(model="llama3.1", model_provider="ollama").bind_tools(allTools) 
graph = StateGraph(HarveyState) 
graph.add_node(startAgent) 
createToolNode = ToolNode([createFile], name="createToolNode", messages_key="harvey_response")  
graph.add_node(createToolNode)
graph.add_edge(START, "startAgent") 
graph.add_edge("startAgent", "createToolNode") 
graph.add_edge("createToolNode", END) 
agent = graph.compile() 

response = agent.invoke({"userQuery": [HumanMessage("make a hello world file in c++ for me please")]})
