from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_evaluation_mlflow import Evaluation
from CNNClassifier import logger

stage_name = "Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info("*"*19)
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e