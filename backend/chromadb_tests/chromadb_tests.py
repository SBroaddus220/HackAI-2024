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

import os
import logging
from typing import List
from pathlib import Path
from dotenv import load_dotenv

# LangChain imports (so many =_=)
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

# Local imports
# from backend.config import LOGGER_CONFIG

# **********
# Sets up logger
logger = logging.getLogger(__name__)


# **********
def load_documents(documents_dir: Path) -> List[Document]:
    """Loads `*.txt` documents from a directory into a list of documents to import into ChromaDB.

    Args:
        documents_dir (Path): Path to directory containing documents.

    Returns:
        list: List of documents to import into ChromaDB.
    """
    # Directory containing the documents
    documents_dir = Path("./documents")

    # Setup for splitting documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

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


def query_with_retrieval(input: str, db, docs, openai_api_key) -> str:
    # Retrieve documents with similar content to input
    logger.info("Retrieving documents with similar content to input...")
    query = input
    retrieved_docs = db.similarity_search(query)
    context = " ".join([doc.page_content for doc in retrieved_docs])
    
    # Create the language model
    
    ## NEED TO CHANGE THIS
    logger.info("Creating language model...")
    llm = ChatOpenAI(openai_api_key=openai_api_key)

    # Create the embeddings
    logger.info("Creating embeddings...")
    embeddings = OpenAIEmbeddings()

    # Create the vector store
    logger.info("Creating vector store...")
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)

    # Create the document chain
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}""")

    # Create the document chain
    logger.info("Creating document and retrieval chain...")
    document_chain = create_stuff_documents_chain(llm, prompt)

    # Create the retrieval chain
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Invoke the chain
    logger.info("Invoking chain...")
    response = retrieval_chain.invoke({"input": input})
    return response["answer"]


# **********
def main():
    pass

# **********
if __name__ == "__main__":
    main()