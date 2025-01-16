# AI Agent for Financial Analysis with Web Search Using Phidata

## Overview

This project showcases the development of AI agents using the Phidata framework to perform web searches and financial analyses. The agents utilize the Groq model for processing and generating responses, integrating tools like DuckDuckGo for web searches and YFinanceTools for financial data analysis.

## Requirements

- Python 3.x
- Phidata library
- Groq model access
- DuckDuckGo tool
- YFinanceTools

## Setup Instructions

1. **Activate Virtual Environment**:  
   Open your terminal and navigate to your project directory. Activate the virtual environment by running the following command:
.\env\Scripts\activate.ps1

2. **Install Dependencies**:  
Install the required packages by running the following command:
pip install -r requirements.txt

3. **Configure API Keys**:  
Create a `.env` file in your project directory and add your API keys as follows:
GROQ_API_KEY=your_groq_api_key_here
Replace `your_groq_api_key_here` with your actual Groq API key.

4. **Set Environment Variable**:  
Set the `GROQ_API_KEY` environment variable by running:
setx GROQ_API_KEY "your_groq_api_key_here"
Or, for the current session:
$env:GROQ_API_KEY = "your_groq_api_key_here"

## Usage

Run the following scripts to interact with the AI agents:

1. **Playground Script**:
python playground.py

2. **Financial Agent Script**:
python financial_agent.py


## Notes

- Ensure that your environment variables are set correctly for the Groq API key.
- The `print_response` method is used to generate and display the agent's response based on the input query.

## References

- [Phidata Documentation](https://docs.phidata.com/)
- [Groq Console](https://console.groq.com/)
- [DuckDuckGo Tool](https://docs.phidata.com/tools/duckduckgo/)
- [YFinanceTools](https://docs.phidata.com/tools/yfinance/)
