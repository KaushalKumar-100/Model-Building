import os
import logging
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG, #debug will print both debug and info
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),  #terminal
        logging.FileHandler("app.log")  #file
        
    ]
)
dataset_path=os.getenv("DATASET_PATH")

logging.info("Loading dataset")
df=pd.read_csv(dataset_path)
logging.info("Dataset loaded successfully")
print(df.head)
