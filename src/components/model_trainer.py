from sklearn.linear_model import LinearRegression
from sklearn.ensemble import (AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor)
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from data_transformation import transformation
from sklearn.metrics import r2_score
from src.exception import CustomException
import sys
from src.utils import save_fxn
import os
from src.logger import logging

def training():
    models = {
        "Random Forest": RandomForestRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "Linear Regression": LinearRegression(),
        "XGBRegressor": XGBRegressor(),
        "AdaBoost Regressor": AdaBoostRegressor(),
    }
    params={
        "Random Forest":{'n_estimators': [8,16,32,64,128,256]},
        "Decision Tree":{'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson']},
        "Gradient Boosting":{'learning_rate':[.1,.01,.05,.001],'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],'n_estimators': [8,16,32,64,128,256]},
        "Linear Regression":{},
        "XGBRegressor":{'learning_rate':[.1,.01,.05,.001],'n_estimators': [8,16,32,64,128,256]},
        "AdaBoost Regressor":{'learning_rate':[.1,.01,0.5,.001],'n_estimators': [8,16,32,64,128,256]}
    }

    train,test,_=transformation()
    x_train=train[:,:-1]
    y_train=train[:,-1]
    x_test=test[:,:-1]
    y_test=test[:,-1]
    maxi=-1
    best_model=''
    for i,j in models.items():
        grid=GridSearchCV(estimator=j,param_grid=params[i],n_jobs=-1,cv=3)
        grid.fit(x_train,y_train)
        y_pred=grid.predict(x_test)
        score=r2_score(y_test,y_pred)
        if score>maxi:
            maxi=score
            best_model=grid.best_estimator_
    if (maxi<0.6):
        raise CustomException('No best model found',sys)
    file_path=os.path.join('artifacts','model.pkl')
    save_fxn(file_path,best_model)
    logging.info(f'Best Score is {maxi}')



training()
