from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import DataIngestion
from CNNClassifier import logger

stage_name = 'Data ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip()
        
        
if __name__ == '__main__':
    try:
        logger.info(f">>>> stage: {stage_name} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage: {stage_name} ended <<<<")
    except Exception as e:
        logger.exception(e)
        raise e