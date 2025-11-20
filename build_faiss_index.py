from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pandas as pd

# 1. Load FAQ / knowledge base data
df = pd.read_csv('data/faq_data.csv')  # Make sure this CSV has a column 'faq_text'
texts = df['faq_text'].tolist()

# 2. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_text(" ".join(texts))

# 3. Generate embeddings
embeddings = OpenAIEmbeddings()
faiss_index = FAISS.from_texts(docs, embeddings)

# 4. Save the FAISS index locally
faiss_index.save_local('faiss_index')

print("FAISS index built and saved successfully!")
