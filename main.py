from CNNCLASIFIER import logger
from CNNCLASIFIER.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNCLASIFIER.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNCLASIFIER.pipeline.stage_03_training import ModelTrainingPipeline
from  CNNCLASIFIER.pipeline.stage_04_evaluation import EvaluationPipeline



STAGE_NAME ="Data ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Training"
try:
      logger.info(f"*******************")
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = ModelTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e






STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e