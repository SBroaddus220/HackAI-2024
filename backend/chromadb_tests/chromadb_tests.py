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
from langchain_openai import OpenAI, ChatOpenAI

from langchain_community.document_loaders import PyPDFLoader

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 500


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

    # Setup for splitting documents into chunks
    # text_splitter = CharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        "gpt2", chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )

    # This will store chunks from all documents
    docs = []

    # Iterate over each text file in the directory
    for file_path in documents_dir.glob(
        "*.txt"
    ):  # Adjust the pattern if your files have a different extension
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

    # Setup for splitting documents into chunks
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        "gpt2", chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )

    # This will store chunks from all documents
    docs = []

    # Iterate over each text file in the directory
    for file_path in documents_dir.glob(
        "*.pdf"
    ):  # Adjust the pattern if your files have a different extension
        logger.info(f"Loading document: {file_path}")
        # Load the document
        loader = PyPDFLoader(str(file_path))
        document_content = loader.load_and_split()

        # Split the current document into chunks
        document_chunks = text_splitter.split_documents(document_content)

        # Add the chunks of the current document to the overall list
        docs.extend(document_chunks)

    return docs


def store_documents(docs: List[Document], collection_name:str) -> Chroma:
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
    db = Chroma.from_documents(docs, embedding_function, collection_name=collection_name)

    return db


def query_with_retrieval(input: str, db, openai_api_key) -> str:
    # Retrieve documents with similar content to input
    logger.info("Retrieving documents with similar content to input...")
    print(db)
    print("--------------------")
    retrieved_docs = db.similarity_search(input)
    
    print(retrieved_docs)
            
    def pretty_print_docs(docs):
        print(
            f"\n{'-' * 100}\n".join(
                [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
            )
        )
    
    # pretty_print_docs(retrieved_docs)
    
    
    context = " ".join([doc.page_content for doc in retrieved_docs])
    
    chat = ChatOpenAI(openai_api_key=openai_api_key)
    
    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage(content=f"Answer the following questions based only on the provided context: {context}"),
        HumanMessage(content=input),
    ]
    

    response  = chat.invoke(messages)

    return response.content



# **********
def main():
    pass


# **********
if __name__ == "__main__":
    main()
