
import os

import logging

import sys 

log_file="logging"

log_path=os.path.join(log_file,".log")

os.makedirs(log_file,exist_ok=True)


format=" %(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s "


logging.basicConfig(
    format=format,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)


logger=logging.getLogger("Churnprediction")