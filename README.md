# Simple AI

Here's a straightforward Python3 example demonstrating how to utilize ChatGPT using Llama Index. In this scenario, we'll outline a process that involves taking a single or multiple PDF files as input and storing them in a local vector database. Then conveniently accessing the chatbot from the command prompt, making it ideal for testing purposes.

## YouTube Video Tutorial for this GitHub Repository
[Simple Chatbot using Llama Index](https://youtu.be/beH56W7rcOQ)

## Installation

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/simple_ai.git 
```
3. use pip or pip3 to install any dependencies.
```bash
pip3 install -r requirements.txt
```

## Usage

Make sure to get an OpenAI key from https://platform.openai.com/account/api-keys

Create a ".env" file and put your OpenAI key in that file
```bash
OPENAI_API_KEY='your key here'
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
