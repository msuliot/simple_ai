# ------ > Run the command below in the terminal, use -- printenv -- to validate OPENAI_API_KEY
# export OPENAI_API_KEY="YOUR KEY HERE"
# put data in data folder

from pathlib import Path
from llama_index import download_loader

PDFReader = download_loader("PDFReader") # https://llamahub.ai

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

loader = PDFReader()
documents = SimpleDirectoryReader('data').load_data()
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist()
print("Done") 