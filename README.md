# Simple AI

Here's a straightforward Python3 example demonstrating how to utilize ChatGPT using Llama Index. In this scenario, we'll outline a process that involves taking a single or multiple PDF files as input and storing them in a local vector database. Then conveniently accessing the chatbot from the command prompt, making it ideal for testing purposes.

## Installation

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/simple_ai.git 
```
3. use pip or pip3 to install any dependencies.
```bash
pip install openai
pip install llama-index
```

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Add your OpenAI Key to the OS environmental variables
```bash
export OPENAI_API_KEY="YOUR_OPEN_AI_KEY"
```
<< OR >>

Add the following to both Python files
```bash
import openai
openai.api_key = "YOUR_OPEN_AI_KEY"
```

**Delete the placeholder-delete-this files in the data and storage directories.**

Then, save any PDFs in the 'data' directory.

Then run your data importer in VS Code or
```bash
python3 data_import.py
```
When the process is complete it will store result in a vector database located in the 'storage' directory

To run the chatbot, use the following command:

```bash
python3 app_cmd.py 'your question'
```

## Notes

[AI Research Notes](https://github.com/msuliot/ai)
