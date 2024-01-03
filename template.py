import os
from pathlib import Path
import logging

# logging screen (it's better than print)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNN_Classifier'

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Creating logic for creating the files
for string in list_of_files:
    filepath = Path(string)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        if os.path.exists(filedir):
            logging.info(f"The directory {filedir} already exists.")
        else:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating empty folder: {filedir}")

            
    if os.path.exists(filepath):
        logging.info(f"File: {filepath} already present.")
        
    else:
        logging.info(f"Creating empty file: {filepath}")
        with open(filepath, 'w') as f:
            pass