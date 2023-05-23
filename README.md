# Simple AI

Here's a straightforward example demonstrating how to utilize ChatGPT within the Llama Index. In this scenario, we'll outline a process that involves taking single or multiple PDF files as input and storing them in a vector database. Then conveniently accessed from the command prompt, making it ideal for testing purposes.

## Installation

1. Clone the repository. 
2. use pip or pip3 to install dependencies

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Add your OpenAI Key to the OS environmental variables
```bash
run export OPENAI_API_KEY="YOUR_OPEN_AI_KEY "
```

Save any PDFs in the 'data' directory.

then run your data importer
```bash
run data_import.py file
```
When the process is complete it will store result in a vector database located in the 'storage' directories

To run the chatbot, use the following command:

```bash
python3 app_cmd.py 'your question'
```