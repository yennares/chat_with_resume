import streamlit as st
import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

# Function to process the uploaded resume
def process_resume(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    return docs

# Streamlit App UI
def main():
    st.header("Resume Assistant using RAG approach", divider="rainbow", anchor=False)
    
    # Get OpenAI API Key from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")

    if not openai_api_key:
        st.error("❌ OpenAI API key not found! Please add your API key to the .env file.")
        st.stop()

    # Check if resume.pdf exists
    resume_path = "resume.pdf"
    if not os.path.exists(resume_path):
        st.error("❌ Resume file 'resume.pdf' not found! Please place your resume file in the project directory.")
        st.stop()

    # Initialize session states
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

    # Auto-process the resume on first load
    if st.session_state.qa_chain is None:
        st.write("🔄 Processing resume...")

        # Process the resume
        documents = process_resume(resume_path)

        # Generate embeddings and create a Chroma retriever
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        vector_store = Chroma.from_documents(documents, embeddings, persist_directory=".chromadb")
        retriever = vector_store.as_retriever()

        # Define a system prompt
        system_prompt="""
        Reader Skill: Leverage your adeptness and summarizing skills to accurately respond to queries regarding Saritha resume.
        Individual Identity: Keep in mind that the resume belongs to an individual named Saritha.
        Conciseness and Relevance: Ensure your responses are concise, relevant, and directly address the query.
        Precision: Provide precise and detailed answers, focusing solely on the information presented in the resume.
        Missing Information: If certain details are absent in the resume, acknowledge it and provide a brief summary of Saritha.
        Positivity: Maintain a positive tone in your responses, aiming to enhance opportunities for Saritha.
        Exclusion of Non-Resume Information: Do not include any information that is not available on the resume.
        Clarity: Responses should be clear and easy to understand.
        Accuracy: Ensure responses accurately reflect the content of the resume.
        Engagement: Provide engaging and informative responses.
        Respectful Language: Use respectful and professional language throughout.
        Singular Pronouns: Utilize singular pronouns (e.g., "He," "Her") instead of plural pronouns (e.g., "They," "Their").
        Markdown Formatting: Present your responses in clear markdown format for easy readability and use sub-headings and lists wherever possible.
        """

        # Customize the PromptTemplate
        prompt_template = PromptTemplate(
            template=f"{system_prompt}\n\nContext: {{context}}\n\nQuestion: {{question}}\nAnswer:",
            input_variables=["context", "question"]
        )

        # Create the QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(temperature=0, openai_api_key=openai_api_key),
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt_template}
        )

        st.session_state.qa_chain = qa_chain
        st.success("✅ Resume processed successfully! You can now ask questions.")

    # Query input and response display
    query = st.text_input("💬 Ask a question about the resume:")
    if query and st.session_state.qa_chain:
        with st.spinner("🔍 Searching for answer..."):
            response = st.session_state.qa_chain(query)
        st.write("### 🤖 Answer:")
        st.write(response["result"])

if __name__ == "__main__":
    main()
