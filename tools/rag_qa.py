from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

class RAGQATool:
    def __init__(self, knowledge_base_path='../data/faq_data.csv'):
        self.embeddings = OpenAIEmbeddings()  # You can replace with sentence-transformers
        self.vector_store = FAISS.load_local('faiss_index', self.embeddings)  # Pre-build index
        self.retriever = self.vector_store.as_retriever()
        self.qa = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
            chain_type="stuff",
            retriever=self.retriever
        )

    def answer(self, query):
        return self.qa.run(query)
