
from crewai import Agent, Crew, Task
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

dummy_agent = Agent(
            role = "Dummy Agent",
            goal = "Test input parameter",
            verbose = True,
            llm = llm,
            backstory = "You are an expert Agent who can demonstrate "
                "input {parameter}"
    )

dummy_task =  Task(
            description = "dummy task who can demonstrate "
                "input {parameter}",
            expected_output = "value of parameter is "
                "{parameter}",
            max_inter = 3,
            agent = dummy_agent
        )

crew = Crew(
        agents=[dummy_agent],
        tasks=[dummy_task],
        verbose=2,
)

result = crew.kickoff(inputs={"parameter": "value"})
print (result)