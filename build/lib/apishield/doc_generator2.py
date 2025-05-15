import os
import openai
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API key securely from .env file
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key is missing in the environment variables")

# Set OpenAI API key
openai.api_key = api_key

# Function to generate documentation from the data
def generate_documentation(data):
    # Combine all data into a formatted string for the AI model
    documentation_data = f"""
    This is a detailed analysis of the API function. Please generate comprehensive documentation based on the above data.

    Function Source Code: {data['sr_code']}
    Imported Modules: {data['imported_modules']}
    Docstring: {data['docstring']}
    Signature: {data['signature']}
    Current File: {data['current_file']}
    Frame: {data['frame']}
    HTTP Method: {data['method']}
    API Path: {data['path']}

    i want also take action if needed to genearate the test cases for the api and check dynamically for the security issues
    """

    # Generate documentation using OpenAI's GPT
    response = openai.Completion.create(
        model='gpt-4o-mini',  # Use the most appropriate model
        prompt=f"Generate API documentation based on the following data:\n{documentation_data}",
        max_tokens=500,  # Limit tokens for reasonable length
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Get the generated documentation from the response
    documentation = response.choices[0].text.strip()

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

