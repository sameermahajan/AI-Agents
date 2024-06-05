"""various tasks"""
from crewai import Task


class BloggingTasks():
    """various tasks useful for blogging"""

    def __init__ (self, website):
        self.website = website

    def summarize_trip_task(self, agent, tools):
        """task that summarizes a trip"""
        
        return Task(
            description = f"""Summarize trip from given blog content. Use the
                tools at your disposal to get the blog content from 
                {self.website} If the blog is NOT about trip,
                DO NOT generate ANY content but keep it blank.""",
            expected_output = """HTML Table with 5 columns of:
                1. travel date. You can get the travel date from the link:
                2. destination
                3. places visited
                4. brief two to three line summary of the trip""",
            max_inter = 3,
            tools = tools,
            agent = agent
        )

    def summarize_trip_with_image_task(self, agent, tools):
        """task that summarizes a trip. It provides a highlight image for
        the trip in the summary."""
        
        return Task(
            description = f"""Summarize trip from given blog content. Use the
                tools at your disposal to get the blog content from 
                {self.website} If the blog is NOT about trip, DO NOT generate
                ANY content but keep it blank.""",
            expected_output = """HTML Table with 5 columns of:
                1. travel date. You can get the travel date from the link:
                2. destination
                3. places visited
                4. brief two to three line summary of the trip
                5. embedded image with hyperlink depicting the trip hightlight. 
                Make sure that the hyperlink is valid. Otherwise do not include 
                it.""",
            max_inter = 3,
            tools = tools,
            agent = agent
        )

    def summarize_trips_task(self, agent, tools):
        """task that summarizes multiple trips"""
        
        return Task(
            description = f"""Summarize trips from given blog content. Use the
                tools at your disposal to get the blog content from
                {self.website} If the blog is NOT about trip,
                DO NOT generate ANY content but keep it blank.""",
            expected_output = """HTML Table with 4 columns of:
                1. travel date. You can get the travel date from the link.
                2. destination
                3. places visited
                4. brief two to three line summary of the trip""",
            max_inter = 3,
            tools = tools,
            agent = agent
        )

    def summariz_trips_with_image_task(self, agent, tools):
        """task that summarizes multiple trips. It provides a highlight image
            for each of the trips in the summary."""
   
        return Task(
            description = f"""Summarize trips from given blog content. Use the
                tools at your disposal to get the blog content from
                {self.website} If the blog is NOT about trip,
                DO NOT generate ANY content but keep it blank.""",
            expected_output = """HTML Table with 5 columns of:
                1. travel date. You can get the travel date from the link.
                2. destination
                3. places visited
                4. brief two to three line summary of the trip
                5. embedded image with hyperlink depicting the trip hightlight. 
                    Make sure that the hyperlink is valid. Otherwise do not 
                    include it.""",
            max_inter = 3,
            tools = tools,
            agent = agent
        )

    def recommend_trip_task(self, agent, tools, next_trip_time, duration):
        """Task that recommends next trip based on previous trips taken,
        time when the trip is planned, interests of the planner, etc."""

        return Task(
            description = f"""Recommend destination of the next trip based on
                previous trips. The next trip is to be planned on 
                {next_trip_time} for {duration}. You can leverage the provided
                tools to learn about previous trips as well as to decide the
                destination for the next trip.""",
            expected_output = "destination of the next trip",
             max_inter = 3,
            tools = tools,
            agent = agent
        )
