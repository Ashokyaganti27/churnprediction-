

from src.churnprediction.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.churnprediction import logger
STAGE_NAME="DATE INGESTION STAGE"

try:
   logger.info(f"Stage {STAGE_NAME} Started")
   data_ingestion=DataIngestionTrainingPipeline()
   data_ingestion.initiate_data_ingestion()
   logger.info(f"Stage {STAGE_NAME} completed")

except Exception as e:
   raise e

