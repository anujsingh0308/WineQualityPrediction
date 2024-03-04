from Wine_Quality_Prediction import logger
from Wine_Quality_Prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_Quality_Prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Wine_Quality_Prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Wine_Quality_Prediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Model Training stage" 

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:  
    logger.exception(e)
    raise e