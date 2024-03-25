import os
import sys
from pydantic import SecretStr

# Get the API key from the environment variables
api_key_str = os.getenv("OPENAI_API_KEY")
key = SecretStr(api_key_str) if api_key_str else None

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_text_splitters import CharacterTextSplitter  # Add this import


def summarize_text(file_path):
    """
    Summarizes the text from the input file using the OpenAI GPT-3.5 model.

    Args:
        file_path (str): Path to the input text file.

    Returns:
        None
    """
    # Define the OpenAIChat model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125",
        temperature=0.7,  # Adjust temperature as needed
        api_key=key,
    )

    # Define prompt templates for the refine method
    question_prompt_template = """
    Please provide a summary of the following text.
    TEXT: {text}
    SUMMARY:
    """

    refine_prompt_template = """
    Write a concise summary of the following text delimited by triple backquotes.
    Return your response in bullet points which cover the key points of the text.
    ```{text}```
    BULLET POINT SUMMARY:
    """

    question_prompt = PromptTemplate(
        template=question_prompt_template, input_variables=["text"]
    )
    refine_prompt = PromptTemplate(
        template=refine_prompt_template, input_variables=["text"]
    )

    # Load text from the specified file
    text_loader = TextLoader(file_path)
    docs = text_loader.load()

    # Initialize the text splitter
    # Adjust chunk_size and chunk_overlap as needed
    chunk_size = 4096  # Max output tokens for GPT-3.5 Turbo
    chunk_overlap = 0
    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    # Split the document into chunks
    split_docs = text_splitter.split_documents(docs)

    # Initialize the summarization chain using the refine method
    refine_chain = load_summarize_chain(
        llm,
        chain_type="refine",
        question_prompt=question_prompt,
        refine_prompt=refine_prompt,
        return_intermediate_steps=True,
    )

    # Perform text summarization
    result = refine_chain({"input_documents": split_docs})

    # Join the list of strings into a single string
    summarized_text = "\n".join(result["intermediate_steps"])

    # Save the summarized content to a new file
    output_file_path = file_path.replace(".txt", "_summarized.txt")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(summarized_text)

    print(f"Summarized content saved to: {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python summarizer.py {text_file}.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    summarize_text(file_path)
