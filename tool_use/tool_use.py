from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

def get_square_and_cube(number):
    return {
        "square": number ** 2,
        "cube": number ** 3
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_square_and_cube",  # Tool name (identifier for calling)
            "description": "Calculate the square and cube of a number",  # Human-readable purpose
            "parameters": {  # JSON schema defining what arguments the tool expects
                "type": "object",
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "The number to process"
                    }
                },
                "required": ["number"]
            }
        }
    }
]

response = client.chat.completions.create(
 model="qwen2.5-coder:32b",
  messages=[
        {"role": "user", "content": "What is the square and cube of 4?"}
    ],
    tools=tools,
    tool_choice="auto"
)

print(response)
print(response.choices[0].message.content)
