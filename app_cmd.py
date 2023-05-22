# ------ > Run the command below in the terminal, use -- printenv -- to validate OPENAI_API_KEY
# export OPENAI_API_KEY="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"

import sys

if len(sys.argv) != 2:
    print("Usage: python3 app_cmd.py 'The Parameter'")
    sys.exit(1)

param = sys.argv[1]

from llama_index import StorageContext, load_index_from_storage
storage_context = StorageContext.from_defaults(persist_dir='./storage')
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query(param)

print(" ")
print("==> Michael AI :)", response)
print(" ")