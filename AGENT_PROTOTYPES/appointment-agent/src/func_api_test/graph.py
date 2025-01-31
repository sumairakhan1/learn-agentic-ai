"""This module defines the state graph for the react agent."""

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import add_messages
from langchain_core.messages import (
    SystemMessage,
    BaseMessage,
    ToolCall,
)
from langgraph.types import interrupt
from langgraph.func import entrypoint # New 

# LLM
llm = ChatOpenAI(model="gpt-4o")

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


@tool
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

def call_llm(messages: list[BaseMessage]):
    """LLM decides whether to call a tool or not"""
    return llm_with_tools.invoke(
        [
            SystemMessage(
                content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
            )
        ]
        + messages
    )

def call_tool(tool_call: ToolCall):
    """Performs the tool call"""

    # Interrupt the workflow to get a review from a human.
    is_approved = interrupt({ # New 
            # Any json-serializable payload provided to interrupt as argument.
            # It will be surfaced on the client side as an Interrupt when streaming data
            # from the workflow.
            "tool_call": tool_call, # The tool call we want reviewed.
            # We can add any additional information that we need.
            # For example, introduce a key called "action" with some instructions.
            "action": "Please approve/reject the tool call",
        })
    
    if is_approved:
        tool = tools_by_name[tool_call["name"]]
        return tool.invoke(tool_call)
    else:
        return "Tool call rejected"

@entrypoint()  
def func_api_test_graph(messages: list[BaseMessage], previous: list[BaseMessage]): 
    """ Tool calling agent """

    # Add previous messages from short-term memory to the current messages
    if previous is not None:
        messages = add_messages(previous, messages)
    
    # Call the LLM
    llm_response = call_llm(messages)

    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_results = [
            call_tool(tool_call) for tool_call in llm_response.tool_calls
        ]
        messages = add_messages(messages, [llm_response, *tool_results])
        llm_response = call_llm(messages)

    messages = add_messages(messages, llm_response)
    return messages


# func_api_test_graph = builder.compile()

# func_api_test_graph.name = "func_api_test"
