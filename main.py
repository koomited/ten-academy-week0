from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_ingestion = DataIngestionPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    
    STAGE_NAME = "Data Validation Stage"

    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_validation = DataValidationPipeline()
        data_validation.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Data Transformation Stage"

    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_transformation = DataTransformationPipeline()
        data_transformation.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Model Trainer Stage"

    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e