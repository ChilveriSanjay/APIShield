import os
import openai
import datetime
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

# Retrieve the API key securely from .env file
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key is missing in the environment variables")

# Set OpenAI API key
openai.api_key = api_key

# Function to generate documentation from the data using LangChain
def generate_documentation(data):
    # Define the prompt template for generating documentation
    documentation_template = """
    You are an AI assistant tasked with generating API documentation based on the provided data.

    The function source code is as follows:
    {sr_code}

    The function imports the following modules:
    {imported_modules}

    The function docstring is:
    {docstring}

    The function signature is:
    {signature}

    The current file is:
    {current_file}

    The current function is being executed with the following details:
    HTTP Method: {method}
    API Path: {path}

    Please generate comprehensive API documentation based on the above data. You may also suggest security checks and test cases that could be beneficial.
    """

    # Initialize LangChain PromptTemplate with the documentation generation prompt
    prompt = PromptTemplate(
        input_variables=["sr_code", "imported_modules", "docstring", "signature", "current_file", "method", "path"],
        template=documentation_template
    )

    # Set up the LLM (using OpenAI's model)
    llm = OpenAI(temperature=0.7, model="gpt-4o-mini")  # Adjust the model as needed

    # Create an LLMChain to execute the prompt and model
    chain = LLMChain(llm=llm, prompt=prompt)

    # Generate the documentation by running the LLMChain
    documentation = chain.run(
        sr_code=data['sr_code'],
        imported_modules=data['imported_modules'],
        docstring=data['docstring'],
        signature=data['signature'],
        current_file=data['current_file'],
        method=data['method'],
        path=data['path']
    )

    return documentation

# Function to write or update the doc_api.txt file
def write_documentation_to_file(documentation):
    doc_filename = "doc_api.txt"
    
    # Get current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check if doc_api.txt exists
    if os.path.exists(doc_filename):
        # Append new documentation with timestamp
        with open(doc_filename, "a") as doc_file:
            doc_file.write(f"\n\n--- Documentation Generated on {current_timestamp} ---\n")
            doc_file.write(documentation)
            doc_file.write("\n\n")
    else:
        # Create a new doc_api.txt file
        with open(doc_filename, "w") as doc_file:
            doc_file.write(f"--- Documentation Generated on {current_timestamp} ---\n")
            doc_file.write(documentation)
            doc_file.write("\n\n")

# Example data to pass to the generate_documentation function
data = {
    'sr_code': 'def simple_view(request):\n    return JsonResponse({"message": "success"})',
    'imported_modules': '["JsonResponse", "RequestFactory"]',
    'docstring': 'This is a simple view to demonstrate the use of decorators.',
    'signature': 'simple_view(request)',
    'current_file': 'views.py',
    'method': 'GET',
    'path': '/api/simple/'
}

# Generate documentation and write it to a file
documentation = generate_documentation(data)
write_documentation_to_file(documentation)
