from agents import BloggingAgents
from crewai import Crew
from tasks import BloggingTasks
from tools import ScrapeWebPage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import sys

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

# website = "https://sameermahajan.wordpress.com/2023/08/12/spirituality-simplified/"
# "https://sameermahajan.wordpress.com/2024/04/08/weekend-in-lonavala/"
website = "https://sameermahajan.wordpress.com/2023/11/14/bits-goa-diwali-vacation/"

if len(sys.argv) > 1:
    website = sys.argv[1]

agents = BloggingAgents(llm)
tasks = BloggingTasks(website)

summarizer_agent = agents.SummarizeTripAgent()
# summarizer_task = tasks.SummarizeTripTask(summarizer_agent, 
#                                        [ScrapeWebPage.get_content])

summarizer_task = tasks.SummarizeTripWithImageTask(summarizer_agent, 
                                        [ScrapeWebPage.get_content_with_URLs])

crew = Crew(
        agents=[summarizer_agent],
        tasks=[summarizer_task],
        verbose=2,
)
            
results = crew.kickoff()
print (results)
# print(summarizer_task.execute())