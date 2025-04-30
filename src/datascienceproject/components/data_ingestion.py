import os
import urllib.request as request
from src.datascienceproject import logger
import zipfile
import shutil
from src.datascienceproject.entity.config_entity import (DataIngestionConfig)


# Component - Data Ingestion
class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            #filename, headers = request.urlretrieve(
                #url = self.config.source_URL,
                #filename = self.config.local_data_file
            #)
            shutil.copy(self.config.source_URL, self.config.local_data_file)
            #logger.info(f"{filename} download! with following info : \n{headers}")
            logger.info(f"File copied successfully from {self.config.source_URL} to {self.config.local_data_file}")
        else:
            logger.info(f"File already exists")

    def extact_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path) 