from src.CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from CNNClassifier.pipeline.stage_04_model_evaluation_mlflow import ModelEvaluationPipeline

stage_name = 'Data ingestion stage'
try:
    logger.info(f">>>> stage: {stage_name} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = 'Prepare base model stage'

try:
    logger.info(f"*"*19)
    logger.info(f">>>> stage: {stage_name} started <<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = 'Training'

try:
    logger.info(f"*"*19)
    logger.info(f">>>> stage: {stage_name} started <<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = 'Evaluation'

try:
    logger.info(f"*"*19)
    logger.info(f">>>> stage: {stage_name} started <<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e