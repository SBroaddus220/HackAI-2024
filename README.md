# AdviseGPT
A project by team "RAGs to Riches" for Ohio State's HackAI 2024 competition.

## Description
This project aims to revolutionize the way advising documents are parsed and understood by leveraging the advanced capabilities of Retrieval Augmented Generation paired with cutting-edge machine learning models (namely models in the GPT series). Advising documents are catalogued and scanned to allow users to ask specific questions about their schedules and receive a detailed response surrounding the available options and schedules.

### Retrieval Augmented Generation Procedure
1. Documents are stored in their respective filetype-based directories under the `documents` directory (e.g. pdf files are stored in the `documents/pdf` directory)
2. Upon the initiation of the web application, the documents are embedded into a `ChromaDB` vector database. These documents can include both `.txt` and `.pdf` files with easy expandability.
3. Once the user inputs a prompt, the backend computes the embeddings of the input and performs a similarity search on the vector database.
4. From the relevant documents retrieved by the similarity search, the split document chunks are then systematically delivered to the AI model before the prompt to allow it to understand how to properly answer the question.

# Installation
This project is divided into two main components: a dynamic and responsive frontend built with Vite, and a robust, scalable Flask backend. In order to start the project, you need to run the Vite instance and the Flask application in different terminals.

This project has been tested on both Windows and Linux.

## Prerequisites
- `npm` 8.19.4+ installed on your machine. Check your Ruby version with:
```bash
npm --version
```

- `python` 3.10+. Check your Python version:
```bash
python3 --version  # Linux
py --version  # Windows
```

## Vite Project Setup
1. Navigate to `vite-project`
```bash
cd vite-project
```

2. Install dependencies
```bash
npm install
```

3. Run the Vite Project
```bash
npm run dev
```

## Flask Project Setup
1. Navigate to the Flask application
```bash
cd backend
```

2. Create a `.env` file following the `.env.template` file. 

3. Install dependencies (A virtual environment is recommended)
```bash
-m pip install -r requirements.txt
```

4. Run Flask application
```bash
flask run
```

# TO DO:
## Backend Changes
- Multiple similarity searches? How can we determine that an AI model has pulled the correct context?
    - Cohere endpoint seems to be a convenient way to rerank documents for better similarity
- Multiple inputs?
- Select other models with inputs for API keys?
    - Currently looking into [Llamafile](https://python.langchain.com/docs/integrations/llms/llamafile)
    - UPDATE: Can't easily run Windows Executable files on WSL. Windows compatibility will be updated in next Langchain release.
        - 
- Select specific parts of documents to input into context ***
    - Made chunks smaller so that documents can be more precise.

- Better ways to catalogue chunks of data
    - Text overlap (langchain)
    - Knowledge graphs (comp)
    - Larger chunks (3.5 can't do this)
    - Ask llm again (moe)
    - Better splitter / embeddings


## Frontend Changes
- Buffer after an input to allow for API to respond
- Add "Chatbot" message interface, not just list of messages
-Add an initial message from the chatbot ("Hello, I can help you with your planning in an engineering major....")

## Misc Changes
- Look for an API for advisor stuff (Buckeyelink)
- Update README with installation details

- OSU Course API Lead: https://www.reddit.com/r/OSU/comments/mlfz2o/osu_courses_api/

## Authors and Acknowledgement
Steven Broaddus  
Ian Stanton
Josh A'Neal-Pack  
Seth Lamancusa


## Contributing
Contributions are welcome! Feel free to also open issues for major changes.
Please add corresponding tests with new features. All tests must pass before submitting a pull request.

1. Fork the Project
2. Create your new Branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a pull request