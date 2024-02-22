
import os

from llama_index.core import Document, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.indices.keyword_table import GPTKeywordTableIndex
from llama_index.core.indices.tree import GPTTreeIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding

documents = SimpleDirectoryReader('data').load_data()

api_key = "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"
os.environ['OPENAI_API_KEY'] =api_key
embed_model = OpenAIEmbedding(api_key=api_key)

# vector_store_index = VectorStoreIndex.from_documents(documents)

# keyword_index = GPTKeywordTableIndex.from_documents(documents)

# tree_index = GPTTreeIndex.from_documents(documents)


# query_engine = index.as_query_engine()


# query_engine = index.as_query_engine(response_mode="tree_summarize")
# response = query_engine.query("What is creative destruction according to the document?")
# response_text = response.response


# response.source_nodes[0]