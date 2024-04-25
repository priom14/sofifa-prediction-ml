import os 
import sys

from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.utils import convert_to_millions,convert_to_dollars
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion started!")
        try:
            df = pd.read_csv('notebook\data\sofifa.player_updated.csv')
            logging.info("Reading the dataset completed.")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)
            
            logging.info('Feature Engineering Started.')
            df['pos1'] = df['position'].str.split().str[0]
            df['pos2'] = df['position'].str.split().str[1]
            df['age'] = df['age'].astype(int)
            df['base_potential'] = df['base'].str.split(r'[+-]').str[0].astype(int)
            df['potential'] = df['potential'].str.split(r'[+-]').str[0].astype(int)
            df['hieght'] = df['hieght'].str.split('/').str[0].str.split('cm').str[0].astype(int)
            df['weight'] = df['weight'].str.split('/').str[0].str.split('kg').str[0].astype(int)
            df['market_value_millions'] = df['mValue'].apply(convert_to_millions)
            df['wages_dollars'] = df['wage'].apply(convert_to_dollars)
            df['release_clause'] = df['rc'].apply(convert_to_millions)
            df.loc[df['pos2'].isnull(), 'pos2'] = 'None'
            columns = ['_id','name','base','id','mValue','wage','rc','position', 'pos2']
            df = df.drop(columns=columns)
            
            # logging.info(f"{df.isnull().sum()}")
            
            logging.info('Feature Engineering Completed.')
            
            df.to_csv(self.ingestion_config.raw_data_path, index= False, header= True)
            
            logging.info("Train test split initiated!")
            
            train_set, test_set = train_test_split(df,test_size=0.22, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
            
            logging.info("Ingestion of data is completed")
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_traner(train_arr, test_arr))
    
    
    
    
    