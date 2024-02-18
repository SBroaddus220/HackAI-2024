#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests utilizing the ChromaDB vector store and the OpenAI language model with LangChain.

The following details the retrieval process:
- Documents are loaded into a ChromaDB instance.
    - Note that this is a vectorstore by the LangChain community rather than one actually from `chromadb`
- A query is made to the ChromaDB instance to retrieve documents with similar content to the query.
- The retrieved documents are combined into a single document, split into chunks.
- The chunks are fed into the OpenAI language model as context.
- The query is fed into the OpenAI language model as input.
- The response from the OpenAI language model is printed.
"""

import logging
from typing import List
from pathlib import Path

# LangChain imports
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI

from langchain_community.document_loaders import PyPDFLoader

CHUNK_SIZE = 1000


# Local imports
# from backend.config import LOGGER_CONFIG

# **********
# Sets up logger
logger = logging.getLogger(__name__)


# **********
def load_txt_documents(documents_dir: Path) -> List[Document]:
    """Loads `*.txt` documents from a directory into a list of documents to import into ChromaDB.

    Args:
        documents_dir (Path): Path to directory containing documents.

    Returns:
        list: List of documents to import into ChromaDB.
    """
    # Directory containing the documents
    documents_dir = Path("./documents/txt")

    # Setup for splitting documents into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        'gpt2', chunk_size=CHUNK_SIZE, chunk_overlap=0
    )

    # This will store chunks from all documents
    docs = []

    # Iterate over each text file in the directory
    for file_path in documents_dir.glob('*.txt'):  # Adjust the pattern if your files have a different extension
        logger.info(f"Loading document: {file_path}")
        # Load the document
        loader = TextLoader(str(file_path))
        document_content = loader.load()
        
        # Split the current document into chunks
        document_chunks = text_splitter.split_documents(document_content)
        
        # Add the chunks of the current document to the overall list
        docs.extend(document_chunks)
        
    return docs

def load_pdf_documents(documents_dir: Path) -> List[Document]:
    """Loads `*.pdf` documents from a directory into a list of documents to import into ChromaDB.

    Args:
        documents_dir (Path): Path to directory containing documents.

    Returns:
        list: List of documents to import into ChromaDB.
    """
    # Directory containing the documents
    documents_dir = Path("./documents/pdf")

    # Setup for splitting documents into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        'gpt2', chunk_size=100, chunk_overlap=0
    )

    # This will store chunks from all documents
    docs = []

    # Iterate over each text file in the directory
    for file_path in documents_dir.glob('*.pdf'):  # Adjust the pattern if your files have a different extension
        logger.info(f"Loading document: {file_path}")
        # Load the document
        loader = PyPDFLoader(str(file_path))
        document_content = loader.load_and_split()
        
        # Split the current document into chunks
        document_chunks = text_splitter.split_documents(document_content)
        
        # Add the chunks of the current document to the overall list
        docs.extend(document_chunks)
        
    return docs


def store_documents(docs: List[Document]) -> Chroma:
    """Stores documents in a ChromaDB instance.

    Args:
        docs (List[Document]): List of documents to store.
        
    Returns:
        Chroma: ChromaDB instance.
    """
    # Create the embeddings
    logger.info("Creating embedding function...")
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Store the documents
    logger.info("Storing documents in ChromaDB...")
    db = Chroma.from_documents(docs, embedding_function)
    
    return db


def query_with_retrieval(input: str, db, openai_api_key) -> str:
    # Retrieve documents with similar content to input
    logger.info("Retrieving documents with similar content to input...")
    retrieved_docs = db.similarity_search(input)
    
    # ****
    # Test using Cohere to compress and rerank the documents
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import TextLoader
    from langchain_community.embeddings import CohereEmbeddings
    from langchain_community.vectorstores import FAISS
    
    from langchain.retrievers import ContextualCompressionRetriever
    from langchain.retrievers.document_compressors import CohereRerank
    from langchain_community.llms import Cohere
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_documents(retrieved_docs)
    retriever = FAISS.from_documents(texts, CohereEmbeddings()).as_retriever(
        search_kwargs={"k": 20}
    )
    docs = retriever.get_relevant_documents(input)
    
    compressor = CohereRerank()
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )
    retrieved_docs = compression_retriever.get_relevant_documents(
        input
    )
    # ****
            
    def pretty_print_docs(docs):
        print(
            f"\n{'-' * 100}\n".join(
                [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
            )
        )
    
    pretty_print_docs(retrieved_docs)
    
    
    context = " ".join([doc.page_content for doc in retrieved_docs])
    
    # Create the language model
    logger.info("Creating language model...")
    llm = OpenAI(openai_api_key=openai_api_key)

    # Formulate the prompt with context and question
    print(input)
    messages = f"""Answer the following questions based only on the provided context:

                    {context}
                    
                    Question: {input}"""

    # Invoke the language model with the prompt
    logger.info("Invoking language model with prompt...")
    response = llm.invoke(messages)

    return response


# **********
def main():
    pass

# ********** 
if __name__ == "__main__":
    main()
