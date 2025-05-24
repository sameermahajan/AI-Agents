from langchain.tools import tool

@tool
def calculate(expression: str) -> str:
    """Evaluates a math expression."""
    try:
        return str(eval(expression))
    except:
        return "Error evaluating expression"

from langchain.chat_models import init_chat_model

llm = init_chat_model("qwen2.5-coder:32b", model_provider="ollama")

tools = [calculate]
llm = llm.bind_tools(tools)
response = llm.invoke("What is 5 * (7 + 3)?")
print ("response is ", response)
print("========================")
print ("tool calls are ", response.tool_calls)
print("========================")
output = []

for tool_call in response.tool_calls:
    selected_tool = {"calculate": calculate}[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
    print("tool call result is ", tool_msg)
    print("========================")
    output.append(tool_msg.content)

print("Final answer = ", output)
