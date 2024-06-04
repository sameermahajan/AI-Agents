from crewai import Task


class BloggingTasks():

    def __init__ (self, website):
        self.website = website

    def SummarizeTripTask(self, agent, tools):
        return Task(
            description=f"""Summarize trip from given blog content. Use the 
                tools at your disposal to get the blog content from 
                {self.website} If the blog is NOT about trip, 
                DO NOT generate ANY content but keep it blank.""",
            expected_output="""HTML Table with 5 columns of:
                1. travel date. You can get the travel date from the link:
                2. destination
                3. places visited
                4. brief two to three line summary of the trip""",
            max_inter=3,
            tools=tools,
            agent=agent)

    def SummarizeTripWithImageTask(self, agent, tools):
        return Task(
            description=f"""Summarize trip from given blog content. Use the 
                tools at your disposal to get the blog content from 
                {self.website} If the blog is NOT about trip, DO NOT generate 
                ANY content but keep it blank.""",
            expected_output="""HTML Table with 5 columns of:
                1. travel date. You can get the travel date from the link:
                2. destination
                3. places visited
                4. brief two to three line summary of the trip
                5. embedded image with hyperlink depicting the trip hightlight. 
                Make sure that the hyperlink is valid. Otherwise do not include 
                it.""",
            max_inter=3,
            tools=tools,
            agent=agent)
    
    def SummarizeTripsTask(self, agent, tools):
        return Task(
        description=f"""Summarize trips from given blog content. Use the 
            tools at your disposal to get the blog content from
            {self.website} If the blog is NOT about trip, 
            DO NOT generate ANY content but keep it blank.""",
          expected_output="""HTML Table with 4 columns of:
            1. travel date. You can get the travel date from the link.
            2. destination
            3. places visited
            4. brief two to three line summary of the trip""",
        max_inter=3,
        tools=tools,
        agent=agent)
    
    def SummarizeTripsWithImageTask(self, agent, tools):
        return Task(
        description=f"""Summarize trips from given blog content. Use the 
            tools at your disposal to get the blog content from
            {self.website} If the blog is NOT about trip, 
            DO NOT generate ANY content but keep it blank.""",
          expected_output="""HTML Table with 5 columns of:
            1. travel date. You can get the travel date from the link.
            2. destination
            3. places visited
            4. brief two to three line summary of the trip
            5. embedded image with hyperlink depicting the trip hightlight. 
                Make sure that the hyperlink is valid. Otherwise do not include 
                it.""",
        max_inter=3,
        tools=tools,
        agent=agent)
