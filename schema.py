from dataclasses import dataclass 
from typing import TypedDict, Annotated, List
from langchain.messages import HumanMessage, AIMessage 
import operator 

class HarveyState(TypedDict): 
    userQuery: list[HumanMessage]
    harvey_response: list[AIMessage] 






