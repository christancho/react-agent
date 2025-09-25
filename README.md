# ReAct Agent

A Python implementation of a ReAct (Reasoning and Acting) agent using LangChain and OpenAI. This agent can search Wikipedia and answer complex questions by reasoning through the search results step-by-step.

## Features

- 🤖 ReAct (Reasoning and Acting) agent implementation
- 🔍 Wikipedia search and lookup capabilities
- 🧠 OpenAI GPT-3.5-turbo model integration
- 🔧 Environment variable configuration
- 📚 Professional project structure
- ✅ Fully tested and working

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Setup

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   nano .env
   ```
   
   Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Usage

Run the ReAct agent:

```bash
python react-agent.py
```

The agent will process the example question about David Chanoff and the U.S. Navy admiral, demonstrating its reasoning and acting capabilities.

## How it Works

1. **Search Tool**: The agent can search Wikipedia for relevant information
2. **Lookup Tool**: The agent can look up specific articles or sections
3. **Reasoning**: The agent uses the ReAct framework to reason about what information it needs
4. **Acting**: The agent takes actions (search/lookup) based on its reasoning
5. **Answer**: The agent provides a final answer based on the information gathered

## Project Structure

```
ReAct Agent/
├── react-agent.py      # Main script
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .env               # Your actual environment variables (not in git)
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Dependencies

- `openai>=1.6.1,<2.0.0`: OpenAI API client
- `wikipedia==1.4.0`: Wikipedia API wrapper
- `langchain==0.1.0`: Framework for building LLM applications
- `langchain-openai`: OpenAI integration for LangChain
- `langchain-community`: Community tools and utilities
- `langchainhub`: LangChain Hub integration
- `python-dotenv==1.0.0`: Environment variable management

## Example Output

```
🤖 ReAct Agent is thinking...
Question: Author David Chanoff has collaborated with a U.S. Navy admiral who served as the ambassador to the United Kingdom under which President?
--------------------------------------------------

> Entering new AgentExecutor chain...
I need to find out more about David Chanoff and his collaboration with a U.S. Navy admiral...
Action: Lookup
Action Input: David Chanoff
Observation: [Wikipedia search results about David Chanoff]
I need to find more information about David Chanoff's collaboration with a U.S. Navy admiral...
Action: Lookup
Action Input: William J. Crowe
Observation: [Wikipedia search results about William J. Crowe]
I now know that David Chanoff collaborated with U.S. Navy Admiral William J. Crowe, who served as the ambassador to the United Kingdom under President Bill Clinton.
Final Answer: President Bill Clinton

> Finished chain.
--------------------------------------------------
Answer: President Bill Clinton
```

## Customization

To ask different questions, modify the `question` variable in `react-agent.py`:

```python
question = "Your question here"
```

### Example Questions for Testing

Here are some medium-difficulty questions that effectively demonstrate the ReAct agent's reasoning capabilities:

**Art History**: "Which Italian city was Michelangelo working in when he painted the ceiling of the Sistine Chapel, and what was the name of the Pope who commissioned this work?"

**Martial Arts**: "What is the name of the martial art style that Bruce Lee developed, and which traditional Chinese martial art did he study under Ip Man before creating his own system?"

**Statistics**: "Who developed the statistical method known as the t-test, and what was the name of the brewery where this statistician worked when he created this important statistical tool?"

These questions require multi-step reasoning, information synthesis, and demonstrate the agent's ability to connect different pieces of information from Wikipedia searches.

## Notes

- Make sure to keep your `.env` file secure and never commit it to version control
- The agent uses the `gpt-3.5-turbo` model for cost-effectiveness
- Verbose mode is enabled to show the agent's reasoning process
- The agent uses a custom ReAct prompt template for Wikipedia research
