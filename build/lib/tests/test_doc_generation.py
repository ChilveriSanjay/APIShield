# tests/test_doc_generation.py
import pytest
from apishield.doc_generator2 import generate_openapi_docs, validate_openapi_schema

# Test if OpenAPI documentation is generated correctly
def test_generate_openapi_docs():
    generate_openapi_docs()  # This will create openapi.json
    # Check if the file was created
    try:
        with open('openapi.json', 'r') as f:
            assert f.read() is not None, "OpenAPI documentation is empty"
    except FileNotFoundError:
        pytest.fail("OpenAPI documentation file not found")

# Test OpenAPI schema validation
def test_validate_openapi_schema():
    generate_openapi_docs()  # Generate the OpenAPI docs
    validate_openapi_schema()  # Validate the generated docs
    # If validation fails, it will raise an exception
    assert True  # If no exception is raised, the test passes
