import os
import sys
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def convert_to_millions(value):
    if 'M' in value:
        return float(value.replace('M', ''))
    elif 'K' in value:
        return float(value.replace('K', '')) / 1000  # Convert K to M
    else:
        return float(value)
    
    

def convert_to_dollars(value):
    if 'K' in value:
        return float(value.replace('K', '')) * 1000  # Convert K to dollars (multiply by 1000)
    else:
        return float(value)
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok= True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_modell_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score
        
        return report
        
    except Exception as e:
        raise CustomException(e,sys)