from src.CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline

stage_name = 'Data ingestion stage'
try:
    logger.info(f">>>> stage: {stage_name} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = 'Prepare base model stage'

try:
    logger.info(f"*"*19)
    logger.info(f">>>> stage: {stage_name} started <<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = 'Training'

try:
    logger.info(f"*"*19)
    logger.info(f">>>> stage: {stage_name} started <<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e