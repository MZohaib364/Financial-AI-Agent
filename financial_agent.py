from phi.agent import Agent  
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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
    instructions = ["Use tables to display the data."],
    show_tools_calls = True,
    markdown = True
)


multi_ai_agent = Agent(
    team = [Web_Search_Agent, Financial_Agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions = ["Always include sources.", "Use tables to display the data."],
    show_tool_calls=True,
    markdown = True
)

# multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA.", stream=True)


multi_ai_agent.print_response("Give current price of Apple in PKR and USD.", stream=True)