import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]:%(message)s:'
)

project_name="Summarizer"
list_of_files=[
    ".github/workflows/.gitkeep",# Helps for CI/CD deployemet to cloud
    f"src/{project_name}/__init__.py",# init.py is a constructor file which is needed to create local packages which can be imported
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
#Docker can help package your application along with its dependencies and configurations, making it easier to deploy consistently across different environments.
# Docker containers ensure that your application runs the same way regardless of the environment, which reduces the "it works on my machine" problem. 
#Dockerfile might include instructions to:
# Specify a base image (e.g., a specific version of Python or a Linux distribution).
# 1) Install dependencies using package managers (e.g., pip or apt-get).
# 2) Copy application code and files into the image.
# 3) Set environment variables.
# 4) Define commands to start the application when the container is run.


for files in list_of_files:
    filepath=Path(files)# This code basically handles the forward slashes for files and folder.That is paths
    filedir,filename=os.path.split(files)#splitting folder and file

    if(filedir!=""): #This is the code for folder creation whre I checked if my folder is present or not.
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file: {filename}")

    if(not os.path.exists(files)) or (os.path.getsize(files)==0):
        with open(files, 'w') as f:
            pass
        logging.info(f"Creating empty file: {files}")
    else:
        logging.info(f"File already exists: {files}")

# This logging is a good practice as a software developer as it helps to understand the functioning of the code as our program starts
# As well as understand and debug

