"""Recommend next trip"""

import sys

from crewai import Crew
from crewai_tools import FileReadTool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from agents import BloggingAgents
from tasks import BloggingTasks

load_dotenv()

NEXT_TRIP_TIME = "next summer"
DURATION = "8-10 days"

if len(sys.argv) > 1:
    NEXT_TRIP_TIME = sys.argv[1]

if len(sys.argv) > 2:
    DURATION = sys.argv[2]  

llm = ChatOpenAI(model="gpt-4")
previous_trips = FileReadTool("./trip_summaries_with_images.html")

agents = BloggingAgents(llm)
tasks = BloggingTasks("")

recommender_agent = agents.recommend_trip()
recommender_task = tasks.recommend_trip_task(recommender_agent,
                                             [previous_trips],
                                             NEXT_TRIP_TIME,
                                             DURATION)

crew = Crew(
        agents=[recommender_agent],
        tasks=[recommender_task],
        verbose=2,
)

results = crew.kickoff()
print (results)
