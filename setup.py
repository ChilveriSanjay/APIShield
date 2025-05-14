# setup.py
from setuptools import setup, find_packages

setup(
    name="apishield",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "Django",
        "djangorestframework",
        "pylint",
        "black",
        "bandit",
        "vulture",
        "mypy",
        "pytest",
        "requests",
        "langchain"
    ],
    entry_points={
        'console_scripts': [
            'apishield=apishield.cli:run_dynamic_analysis',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Operating System :: OS Independent",
    ],
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sanjay Chilveri",  # Replace with your name
    author_email="chilverisanjay17@gmail.com",  # Replace with your email
    description="A tool for dynamic and static code analysis, security checks, and documentation generation for Django REST Framework APIs.",
)
