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
            llm = self.llm,
            backstory = """You are an expert Trip Summarizer who can summarize 
                trip from the given blog content"""
    )

    def summarize_trips_agent(self):
        """Agent that summarizes multiple trips."""
        
        return Agent(
            role = "Trip Summarizer",
            goal = "Summarize trips from given blog content",
            verbose = True,
            llm = self.llm,
            backstory = """You are an expert Trip Summarizer who  can summarize 
                trips from the given blog content"""
    )

    def recommend_trip(self):
        """Agent that recommends trip based on past trips, season, interests,
            etc."""
        
        return Agent(
            role = "Trip Recommender",
            goal = "Recommend trip based on previous trips, season, interests",
            verbose = True,
            llm = self.llm,
            backstory = """You are an expert trip recommender who can
                recommend next trip based on previous trips, time when the
                trip is to be made and interests of the planner"""
        )
    
    def create_blog(self):
        """Agent that creates a blog for given travel itinerary"""

        return Agent(
            role = "Travel Blogger",
            goal = "Create travel blog for given itinerary",
            verbose = True,
            llm = self.llm,
            backstory = """You are an expert travel blogger. Make use of the
                given itinerary for the destination and visited places to
                blog about. Get information about the places using internet
                search. Keep the blog interesting and engaging.""",
        )

    def create_blog_with_images(self):
        """Agent that creates a blog for given travel itinerary"""

        return Agent(
            role = "Travel Blogger",
            goal = "Create travel blog for given itinerary",
            verbose = True,
            llm = self.llm,
            backstory = """You are an expert travel blogger. Make use of the
                given itinerary for the destination and visited places to
                blog about. Get information about the places using internet
                seaarch. Also get images from the internet to embed in the
                blog to make it engaging.""",
        )
