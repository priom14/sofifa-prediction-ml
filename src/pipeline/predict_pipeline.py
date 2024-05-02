import sys
import os

import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object



class PredictPipieline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
class CustomData:
    def __init__(self,
        pos1 : str,
        age : str,
        base_potential : int,
        potential : int,
        growth : int,
        height : int,
        weight : int,
        foot : str,
        wage : int,
        release_clause : str):
        self.pos1 = pos1
        self.age = age
        self.base_potential = base_potential
        self.potential = potential
        self.growth = growth
        self.height = height
        self.weight = weight
        self.foot= foot
        self.wage = wage
        self.release_clause = release_clause

    def get_data_as_dataframe(self):
        try:
            
            customdata_dict = {
                "pos1" : [self.pos1],
                "age" : [self.age],
                "base_potential" : [self.base_potential],
                "potential" : [self.potential],
                "growth" : [self.growth],
                "hieght" : [self.height],
                "weight" : [self.weight],
                "foot" : [self.foot],
                "wages_dollars" : [self.wage],
                "release_clause" : [self.release_clause]
            }
            logging.info("Test data inserted and created as a dataframe.")
            return pd.DataFrame(customdata_dict)
            
        except Exception as e:
            raise CustomException(e,sys)


