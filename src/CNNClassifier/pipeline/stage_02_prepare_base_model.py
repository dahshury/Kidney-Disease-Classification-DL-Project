from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel
from CNNClassifier import logger

stage_name = 'Prepare base model stage'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
        
if __name__ == '__main__':
    try:
        logger.info(f"*"*19)
        logger.info(f">>>> stage: {stage_name} started <<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage: {stage_name} ended <<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e