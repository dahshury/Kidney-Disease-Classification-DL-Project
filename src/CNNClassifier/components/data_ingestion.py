import os
import zipfile
import gdown
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_data(self) -> str:
        """fetsh data from URL"""
        if not self.config.skip_down:
            try:
                data_URL = self.config.source_URL
                zip_download_dir = self.config.local_data_file
                os.makedirs("/artifacts/data_ingestion", exist_ok=True)
                logger.info(f"Downloading data from: {data_URL} into file: {zip_download_dir}")
                
                file_ID = data_URL.split('/')[-2]
                prefix_id = 'https://drive.google.com/uc?/export=download&id='
                gdown.download(prefix_id+file_ID, zip_download_dir)
                logger.info(f"Downloaded data from: {data_URL} into file: {zip_download_dir}")
                
            except Exception as e:
                raise e
        
        else:
            logger.info(f"Data download skipped due to config.yaml skip_down being enabled.")
            
    def extract_zip(self):
        """extracts zip file into the data directory"""
        
        if not self.config.skip_down:
            unzip_dir = self.config.unzip_dir
            os.makedirs(unzip_dir, exist_ok=True)
            
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
                
            logger.info(f"Downloaded data extracted from: {self.config.unzip_dir} into: {unzip_dir}")
            
        else:
            logger.info(f"Data extraction skipped due to config.yaml skip_down being enabled.")
