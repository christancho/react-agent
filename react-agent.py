import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor, Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please create a .env file with your API key.")

wikipedia = WikipediaAPIWrapper()

def search_wikipedia(query: str) -> str:
    """Search Wikipedia for information about a topic."""
    return wikipedia.run(query)

def lookup_wikipedia(term: str) -> str:
    """Look up a specific term in Wikipedia."""
    return wikipedia.run(term)

tools = [
    Tool(
        name="Search",
        func=search_wikipedia,
        description="Search Wikipedia for information about a topic. Use this when you need to find general information about something."
    ),
    Tool(
        name="Lookup", 
        func=lookup_wikipedia,
        description="Look up a specific term in Wikipedia. Use this when you need to find detailed information about a specific person, place, or concept."
    )
]
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=api_key)

def main():
    """Main function to run the ReAct agent."""
    # Create a simple ReAct prompt template
    react_prompt = PromptTemplate.from_template("""
You are a helpful assistant that can search Wikipedia to answer questions.

You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}
""")
    
    # Create the ReAct agent
    agent = create_react_agent(llm, tools, react_prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Example question
    question = "Author David Chanoff has collaborated with a U.S. Navy admiral who served as the ambassador to the United Kingdom under which President?"
    
    print("🤖 ReAct Agent is thinking...")
    print(f"Question: {question}")
    print("-" * 50)
    
    # Run the agent
    result = agent_executor.invoke({"input": question})
    
    print("-" * 50)
    print(f"Answer: {result['output']}")

if __name__ == "__main__":
    main()