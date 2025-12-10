from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from loguru import logger

from telegram_agent_aws.config import settings
from telegram_agent_aws.infrastructure.clients.qdrant import get_qdrant_client


# Helper function to load a PDF and split it into chunks
def generate_split_documents():
    # Load the specific PDF file containing the knowledge base
    loader = PyPDFLoader("./data/karan_full_biography.pdf")
    
    # Configure the splitter: 1000 chars per chunk, with 200 chars overlap to maintain context across boundaries
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    # Load the document content
    docs = loader.load()
    
    # Split the document into smaller chunks based on the splitter configuration
    all_splits = text_splitter.split_documents(docs)

    return all_splits


# Main function to run the indexing pipeline
def index_documents():
    # Get the split chunks
    all_splits = generate_split_documents()
    
    # Initialize the embedding model (converts text text chunks into vector embeddings)
    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL, api_key=settings.OPENAI_API_KEY)

    # Store the documents in Qdrant Vector DB
    # This automatically computes embeddings and saves them to the specified collection
    QdrantVectorStore.from_documents(
        documents=all_splits,
        embedding=embeddings,
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY,
        collection_name="telegram_agent_aws_collection",
    )

    logger.info("Documents indexed successfully.")
