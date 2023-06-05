from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from utils.dataset_loader import dataset_loader
from decouple import config
import pinecone
import os

# TODO Hacer variable global para que ejecute solo la primera vez.
#def load_dataset():
    


def index_dataset():

    # Download dataset from AWS S3 bucket
    dataset_loader()

    # Set OPENAI_API_KEY
    os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

    # Load Dataset files directory
    loader = PyPDFDirectoryLoader("./dataset/", recursive=True)

    documents = loader.load()

    # print(docs)

    # Split PDF documents by 1000 characters
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents=documents)

    # Set OPEN_AI Embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002", openai_api_key=config("OPENAI_API_KEY")
    )

    # Set Pinecone Env Variables
    PINECONE_API_KEY = config("PINECONE_API_KEY")
    PINECONE_ENV = config("PINECONE_ENV")
    index_name = "insurance-policies"

    # Init Pinecone Vector DB
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

    # Get the vector store from the documents and the embeddings in the index name provided it
    docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)


    return docsearch

dataset_docs = index_dataset()
