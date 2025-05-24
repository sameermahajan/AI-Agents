from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

def ask_gpt(prompt, temperature=0.7):
    response = client.beta.chat.completions.parse(
        model="qwen2.5-coder:32b",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response

def agent_task(task):
    return ask_gpt(f"You are an expert assistant. Complete the following task:\n\nTask: {task}")

def reflect_on_result(task, result):
    prompt = f"""You tried to complete the following task: "{task}"
Here is your result:
{result}

Reflect on whether this solution was good. If not, explain why and how to improve."""
    return ask_gpt(prompt)

def improve_task(task, reflection):
    prompt = f"""Based on the following reflection, rewrite or improve your approach to the task: "{task}"
Reflection:
{reflection}

Improved attempt:"""
    return ask_gpt(prompt)

# Example usage
task = "Write a short Python function that checks if a number is prime."

print("=== Initial Attempt ===")
initial_result = agent_task(task)
print(initial_result)

print("\n=== Reflection ===")
reflection = reflect_on_result(task, initial_result)
print(reflection)

print("\n=== Improved Attempt ===")
improved_result = improve_task(task, reflection)
print(improved_result)
