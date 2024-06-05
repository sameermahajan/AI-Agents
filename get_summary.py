"""Get summaries of trips"""
import sys

from crewai import Crew
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from agents import BloggingAgents
from tasks import BloggingTasks
from tools import ScrapeWebPage

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

# website = "https://sameermahajan.wordpress.com/2023/08/12/spirituality-simplified/"
# "https://sameermahajan.wordpress.com/2024/04/08/weekend-in-lonavala/"
WEBSITE = "https://sameermahajan.wordpress.com/2023/11/14/bits-goa-diwali-vacation/"

if len(sys.argv) > 1:
    WEBSITE = sys.argv[1]

agents = BloggingAgents(llm)
tasks = BloggingTasks(WEBSITE)

summarizer_agent = agents.summarize_trip_agent()
summarizer_task = tasks.summarize_trip_with_image_task(summarizer_agent,
                                        [ScrapeWebPage.get_content_with_URLs])

crew = Crew(
        agents=[summarizer_agent],
        tasks=[summarizer_task],
        verbose=2,
)

results = crew.kickoff()
print (results)
# print(summarizer_task.execute())
