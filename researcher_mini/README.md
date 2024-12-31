# Overview
Research-Mini is an AI-driven project that automates the process of researching and summarizing information. The workflow involves two intelligent agents working collaboratively to process user input, gather relevant data, and produce concise summaries in a structured format. This project is built using cutting-edge AI frameworks, including LangChain, LangGraph, and LangStudio.

## View The Workflow
Go to ```research_mini.png```

## How It Works
### User Input: 
The user provides a query or topic as input.
### Research Agent: 
The input is passed to a Research Agent, which performs thorough research using tools like DuckDuckGo to gather relevant information on the topic.
### Writer Agent: 
The collected information is handed over to a Writer Agent, which organizes and summarizes the findings into a concise three-paragraph format:
- Introduction: Provides an overview and context of the research.
- Main Findings: Summarizes the core data and explanations.
- Conclusion: Concludes the summary and highlights key takeaways.

## Installing dependencies

```pip install -r requirements.txt```
