"""Blog about a trip"""

import sys

from crewai import Crew
from crewai_tools import FileReadTool
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI

from agents import BloggingAgents
from tasks import BloggingTasks
from tools import ScrapeWebPage

load_dotenv()

llm = ChatOpenAI(model="gpt-4")
trip_itinerary = FileReadTool("./Greece")
search_tool = DuckDuckGoSearchRun()

WEBSITE = "https://sameermahajan.wordpress.com/2023/05/30/\
                sikkim-darjeeling-in-a-week/"
if len(sys.argv) > 1:
    WEBSITE = sys.argv[1]

agents = BloggingAgents(llm)
tasks = BloggingTasks(WEBSITE)

blogger_agent = agents.create_blog()
blogger_task = tasks.travel_blogger_task(blogger_agent,
                                        [trip_itinerary,
                                        search_tool,
                                        ScrapeWebPage.get_content])

crew = Crew(
        agents=[blogger_agent],
        tasks=[blogger_task],
        verbose=2,
)

results = crew.kickoff()
print (results)
