from src.datascienceproject import logger
from src.datascienceproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceproject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascienceproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascienceproject.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.datascienceproject.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

logger.info("Welcome to my custom logging data science")

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Trainer stage"

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model evaluation stage"
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x')
except Exception as e:
    logger.exception(e)
    raise e