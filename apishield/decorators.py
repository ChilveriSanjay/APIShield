# api_security_checker/decorators.py
import inspect
import os
from functools import wraps
from django.http import JsonResponse
from django.conf import settings
import subprocess
import ast
import sys
import logging
from apishield.doc_generator import generate_documentation,write_documentation_to_file

def apishield(view_func):
    """
    Decorator to mark a view function for analysis.
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):

        #payload,request,path
        request = args[0]  # DRF request
        method = request.method
        path = request.path

        # Extract function docstring and signature
        docstring = view_func.__doc__ or "No docstring available."
        signature = str(inspect.signature(view_func))

        # Get the current module (file) and related dependencies
        frame = inspect.currentframe()
        current_file = inspect.getfile(frame.f_globals["__name__"])

        #get the imported files and modules
        imported_modules=frame.f_globals
        
        #Extracting the function code
        print(f"Reviewing API: {view_func.__name__}")
        code=str(inspect.getsource(view_func))
        lines=code.splitlines()
        sr_code=lines[1:]
        sr_code='\n'.join(sr_code)  #SOURCE CODE


        # Analyze the current file 
        files_to_analyze = [current_file]

         # Check for modules that are imported in this file 
        for module_name, module in imported_modules.items():
            if module_name != "__builtins__" and isinstance(module, type(sys)):  # If it's a module
                try:
                    # If it’s a module and exists, add it to the files to analyze
                    module_file = module.__file__
                    if module_file not in files_to_analyze:
                        files_to_analyze.append(module_file)
                except AttributeError:
                    continue

        data = {
        'sr_code': sr_code,
        'imported_modules': imported_modules,
        'docstring': docstring,
        'signature':signature,
        'current_file': current_file,
        'frame': frame,
        'method': method,
        'path': path
        }


        # Generate documentation
        documentation = generate_documentation(data)
        
        # Write documentation to file
        write_documentation_to_file(documentation)
        
        print("Documentation has been generated and saved to doc_api.txt.")

    return wrapper


