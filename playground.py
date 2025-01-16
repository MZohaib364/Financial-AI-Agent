from phi.agent import Agent  
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
import phi
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv 

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

# Web_Search_Agent
Web_Search_Agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for information.",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources."],
    show_tools_calls = True,
    markdown = True
)


# Financial Agent
Financial_Agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True)],
    instructions = ["Use table to display the data."],
    show_tools_calls = True,
    markdown = True
)


app =Playground(agents=[Financial_Agent, Web_Search_Agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)

