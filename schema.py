from dataclasses import dataclass 
from typing import TypedDict, Annotated, List
from langchain.messages import HumanMessage, AIMessage 
import operator 

class HarveyState(TypedDict): 
    userQuery: Annotated[list[HumanMessage], operator.add]
    harvey_response: Annotated[list[AIMessage], operator.add] 






