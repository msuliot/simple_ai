# Simple AI

Here's a straightforward example demonstrating how to utilize ChatGPT using Llama Index. In this scenario, we'll outline a process that involves taking a single or multiple PDF files as input and storing them in a local vector database. Then conveniently accessing the chatbot from the command prompt, making it ideal for testing purposes.

## Installation

1. Clone the repository. 
2. use pip or pip3 to install dependencies

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Add your OpenAI Key to the OS environmental variables
```bash
run export OPENAI_API_KEY="YOUR_OPEN_AI_KEY"
```
<< OR >>

Add the following to both Python files
```bash
import os
os.environ["OPENAI_API_KEY"] = 'YOUR_OPEN_AI_KEY'
```

Then, save any PDFs in the 'data' directory.

Then run your data importer in VS Code or
```bash
run python3 data_import.py
```
When the process is complete it will store result in a vector database located in the 'storage' directories

To run the chatbot, use the following command:

```bash
python3 app_cmd.py 'your question'
```

## Notes

•	ChatGPT - LLMs
    •	https://chat.openai.com (history is reviewable, can delete)
    •	ChatGPT 3.5
    •	ChatGPT 4.0 (PLUS) $20
    •	API and plugins - settings to turn on - waitlist
    •	API Keys https://platform.openai.com 
    •	Models https://platform.openai.com/docs/models/overview

•	Llama Index 
    •	https://pypi.org/project/llama-index 
    •	https://llamahub.ai 

•	Lang Chain
    •	https://python.langchain.com/en/latest/index.html 

•	Pinecone - Vector Database/Storage
    •	https://www.pinecone.io 

•	AI Agents
    •	AutoGPT
        •	https://news.agpt.co 
        •	https://docs.agpt.co/setup/ 
    •	Agent GPT
    •	https://agentgpt.reworkd
