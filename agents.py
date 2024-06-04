from crewai import Agent


class BloggingAgents():

    def __init__ (self, llm):
        self.llm = llm

    def SummarizeTripAgent(self):
        return Agent(
        role = "Trip Summarizer",
        goal = f"Summarize trip from given blog content",
        verbose = True,
        llm=self.llm,
        backstory = f"""You are an expert Trip Summarizer who  can summarize 
            trip from the given blog content"""
    )

    def SummarizeTripsAgent(self):
        return Agent(
        role = "Trip Summarizer",
        goal = f"Summarize trips from given blog content",
        verbose = True,
        llm=self.llm,
        backstory = f"""You are an expert Trip Summarizer who  can summarize 
            trips from the given blog content"""
    )