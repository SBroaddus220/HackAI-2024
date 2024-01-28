from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain


# Load environment variables
load_dotenv()

# Get environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Create the language model
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class technical documentation writer."),
    ("user", "{input}")
])

# Create the output parser
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Manually load the text document
file_path = "text.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Create a Document object from the text content
docs = [Document(page_content=text_content)]

# Create the embeddings
embeddings = OpenAIEmbeddings()

# Create the vector store
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector_store = FAISS.from_documents(documents, embeddings)

# Create the document chain
document_prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")

document_chain = create_stuff_documents_chain(llm, document_prompt)

# Create the retrieval chain
retriever = vector_store.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Example usage
question = "What information is contained in the document?"
response = retrieval_chain.invoke({"input": question})
print(response["answer"])
