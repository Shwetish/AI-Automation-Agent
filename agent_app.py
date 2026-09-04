import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# 1. Load environment variables
env_path = Path(r"C:\AI_Automation_Agent\.env")
load_dotenv(dotenv_path=env_path)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langchain.agents import create_agent

# 2. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[
        logging.FileHandler(r"C:\AI_Automation_Agent\agent_workflow.log"),
        logging.StreamHandler()
    ]
)

# 3. Custom Tool Definition
@tool
def calculate_word_count(text: str) -> int:
    """Calculates word count of given input text."""
    logging.info("Tool Execution: Calculating word count.")
    return len(text.split())

# 4. Main Function
def main():
    logging.info("Initializing Google Gemini AI Automation Agent...")
    
    # Verify API Key
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY is missing from your .env file!")

    # Set up active Gemini model target
    llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", temperature=0)
    
    search_tool = DuckDuckGoSearchRun()
    tools = [search_tool, calculate_word_count]

    system_prompt = (
        "You are an autonomous AI Automation Research Agent. "
        "Break down complex requests, search the web, and return concise research summaries."
    )
    
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )

    # 5. Execute Goal
    user_goal = "Research recent advancements in AI Automation Agents and summarize key trends."
    logging.info(f"Executing goal: '{user_goal}'")

    try:
        response = agent.invoke({"messages": [("user", user_goal)]})
        
        print("\n================ AGENT OUTPUT ================")
        if "messages" in response:
            print(response["messages"][-1].content)
        else:
            print(response)
        print("==============================================\n")
        
        logging.info("Workflow executed successfully.")

    except Exception as e:
        logging.error(f"Execution Error: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()