"""various agents"""

from crewai import Agent


class BloggingAgents():
    """Various agents that help with blogging"""

    def __init__ (self, llm):
        self.llm = llm

    def summarize_trip_agent(self):
        """Agent that summaries a trip."""
        return Agent(
        role = "Trip Summarizer",
        goal = "Summarize trip from given blog content",
        verbose = True,
        llm=self.llm,
        backstory = """You are an expert Trip Summarizer who  can summarize 
            trip from the given blog content"""
    )

    def summarize_trips_agent(self):
        """Agent that summarizes multiple trips."""
        return Agent(
        role = "Trip Summarizer",
        goal = "Summarize trips from given blog content",
        verbose = True,
        llm=self.llm,
        backstory = """You are an expert Trip Summarizer who  can summarize 
            trips from the given blog content"""
    )
