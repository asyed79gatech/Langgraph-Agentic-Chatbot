from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:

    def __init__(self, llm):
        """
        Initializes the AI News nodes with the tavily API
        """
        self.llm = llm
        self.tavily = TavilyClient()

        # This state dict is used in the various following steps of the AI news graph
        self.state = {}


    def fetch_news(self, state:dict) -> dict:
        """
        Fetch AI news based on the frequency provided in the state

        Args:
        state (dict): the state dictionary containing the frequency

        Returns:
        state (dict): A news content contained in a new key in the state called "news content"
        """
        frequency = state["messages"][0].content.lower()
        print(frequency)
        self.state["frequency"] = frequency
        time_range_mapping = {'daily': 'd', 'monthly': 'm', 'weekly': 'w', 'yearly': 'y'}
        days_mapping = {'daily': 1, 'monthly': 30, 'weekly': 7, 'yearly': 365}
        response = self.tavily.search(
            query = "Lates Artificial Intelligence (AI) news gloablly",
            topic= "news",
            time_range=time_range_mapping[frequency],
            days=days_mapping[frequency],
            max_results=20
        )

        state["news_data"] = response.get('results', [])
        self.state["news_data"] = state["news_data"]
        return self.state
    
    def summarize_news(self, state: dict) -> dict:
        """
        Retrieves the AI news content from the state key "news_data" and returns structures summary of the news articles

        Args:
        state (dict): news data from the news_data key of the state dict

        Returns:
        state (dict): adds another key in the state dict containng the summarized news
        """

        news_artices = self.state["news_data"]

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", """Summarize AI news articles into markdown format. For each item include:
             - Date in the format **MM-DD-YYYY** in EST timezone
             - Concise sentence summary from the latest news
             - Sort news by date (latest first)
             - Source url should be given at the end as a link in the format:
             ### [Date]
             - [Summary](URL)"""),
             ("user", "News Articles: \n{articles}")
             ]
        )

        news_artilces_string = "\n\n".join([f"Content: \n{item.get("content", "")} \n\n URL: \n{item.get("url", "")} \n\n Published Date: {item.get("published_date", "")}" for item in news_artices])

        # Summarize using the LLM and the prompt template and the news_articles_string
        summary = self.llm.invoke(prompt_template.format(articles = news_artilces_string))

        state["summary"] = summary
        self.state["summary"] = state["summary"]
        return self.state
    

    def save_news(self, state) -> dict:
        """
        Retrieves the summarized news from the state variable and saves it in a .md file

        Args:
        state (dict): Summarized news from the state variable

        Returns:
        state (dict): updated state dict with a new key indicating the path of the saved file containing the news
        """
        # Extract summary and freqeuncy values from the state dict
        summary = self.state["summary"]
        frequency = self.state["frequency"]

        # Create a .md file in the directory to store the News summary
        filename = f"./AI News/{frequency}_summary.md"
        with open(filename, "w") as f:
            f.write(f"## {frequency.capitalize()} AI News Summary \n\n")
            f.write(summary.content)
        
        # Store the file name and location in the state dict
        self.state["filename"] = filename
        return self.state







