
import os

from pathlib import Path


project_name="churnprediction"

from src.churnprediction import logger


list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "research/research.ipynb"
]


for files in list_of_files:
    filepath=Path(files)

    folder, filename =os.path.split(filepath)

    if folder!="":
        os.makedirs(folder, exist_ok=True)

        logger.info(f"folder {folder} is created for {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            logger.info(f" filepath {filepath} created ")
    
    else:
        logger.info(f"filepath {filepath} is already created")
