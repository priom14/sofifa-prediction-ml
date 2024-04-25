import os
import sys
from dataclasses import dataclass
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


from src.utils import save_object, evaluate_model
from src.exception import CustomException
from src.logger import logging


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    
    def initiate_model_traner(self, train_array, test_array):
        try:
            logging.info("Spliting Training and test input data.")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {
                "Linear Regression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "KNN": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "Random Forest": RandomForestRegressor()
            }
            
            logging.info("Model evaluation started.")
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            
            best_model_score = max(sorted(model_report.values()))
            
            logging.info("Best model computed.")
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            
            best_model = models[best_model_name]
            
            if best_model_score<0.6:
                raise CustomException("No best model found.")
            
            logging.info("Best model found on both train and test dataset")      
            
            save_object(
                file_path= self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )
            
            predicred = best_model.predict(X_test)
            
            r2_square = r2_score(y_test, predicred)
            
            return r2_square            
            
        except Exception as e:
            raise CustomException(e,sys)    