from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_training import Training
from CNNClassifier import logger

stage_name = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_val_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f"*"*19)
        logger.info(f">>>> stage: {stage_name} started <<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e