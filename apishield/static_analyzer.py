# api_security_checker/security_engine.py
import requests
from .utils import introspect_view
import subprocess
import ast

def  static_analysis(files_to_analyze):

    for file_path in files_to_analyze:

        analysis_results = {}

       # Pylint: Analyzes Python code for errors and code quality
        pylint_result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
        analysis_results['pylint'] = pylint_result.stdout if pylint_result.returncode == 0 else pylint_result.stderr

        # Black: Checks if the code is formatted according to Black's style
        black_result = subprocess.run(['black', '--check', file_path], capture_output=True, text=True)
        analysis_results['black'] = black_result.stdout if black_result.returncode == 0 else black_result.stderr

        # Bandit: Performs a security analysis to find potential vulnerabilities
        bandit_result = subprocess.run(['bandit', '-r', file_path], capture_output=True, text=True)
        analysis_results['bandit'] = bandit_result.stdout if bandit_result.returncode == 0 else bandit_result.stderr

        # Vulture: Finds unused code (functions, variables, etc.) in the Python code
        vulture_result = subprocess.run(['vulture', file_path], capture_output=True, text=True)
        analysis_results['vulture'] = vulture_result.stdout if vulture_result.returncode == 0 else vulture_result.stderr

        # Mypy: Static type checking to ensure type correctness in Python code
        mypy_result = subprocess.run(['mypy', file_path], capture_output=True, text=True)
        analysis_results['mypy'] = mypy_result.stdout if mypy_result.returncode == 0 else mypy_result.stderr

        # Pytest: Runs the unit tests for the code
        pytest_result = subprocess.run(['pytest', '--maxfail=1', '--disable-warnings', '-q', file_path], capture_output=True, text=True)
        analysis_results['pytest'] = pytest_result.stdout if pytest_result.returncode == 0 else pytest_result.stderr

        

        return analysis_results
