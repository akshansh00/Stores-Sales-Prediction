
from sales.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig 
from sales.util.util import read_yaml_file
from sales.constant import *
from sales.exception import SalesException
import os,sys
from sales.logger import logging

class Configuration:

    def __init__(self,
        config_file_path:str =CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP
        )-> None:
        try:
            self.config_info  = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise SalesException(e,sys) from e


        

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY],
            data_ingestion_info[DATA_INGESTION_RAW_DATA_FILE_NAME_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
            os.makedirs(os.path.dirname(raw_data_dir), exist_ok=True)
            os.makedirs(os.path.dirname(ingested_test_dir), exist_ok=True)
            os.makedirs(os.path.dirname(ingested_train_dir), exist_ok=True)

            data_ingestion_config=DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise SalesException(e,sys) from e
        

    def get_data_validation_config(self)-> DataValidationConfig:
        try:
            pass
        except Exception as e:
            raise SalesException (e,sys) from e 

    def get_data_transformation_config(self)-> DataTransformationConfig:
        pass

    def get_model_trainer_config(self)-> ModelTrainerConfig :
        pass

    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)-> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)-> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            os.makedirs(artifact_dir, exist_ok=True)

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise SalesException(e,sys) from e
            
             