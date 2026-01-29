

import os
import yaml
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from src.churnprediction import logger
import json
import joblib

@ensure_annotations

def read_yaml(file_path :Path)->ConfigBox:

    try:

        with open(file_path) as data:

            file =yaml.safe_load(data)

            logger.info(f" file path {file_path} loaded successfully ")

            return ConfigBox(file)
        
    except Exception as e:

        raise e
    
@ensure_annotations

def create_directories(folders: list):
     
    for filepath in folders:

        os.makedirs(filepath,exist_ok=True)

        logger.info(f" folder is created {filepath}")

@ensure_annotations

def save_json(path: Path, data:dict):

    with open(path,"w") as file:

        json.dump(data,file,indent=4)

    logger.info(f"data converted to json in {path}")

@ensure_annotations

def load_json(path: Path)->ConfigBox:

    with open(path) as file:

        data=json.load(file)

    logger.info(f"json file loaded succfully")

    return ConfigBox(data)

@ensure_annotations

def save_model(path: Path, data: any):

    joblib.dump(value=data,filename=path)

    logger.info(f"mdoel saved in {path}")


@ensure_annotations

def load_model(path:Path):

    data=joblib.load(path)

    logger.info(f"model loaded from {path}")

    return data


        
