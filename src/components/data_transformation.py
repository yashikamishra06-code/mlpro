from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
from src.utils import save_fxn
import os
from data_ingestion import ingestion
def transformation():
    numeric_columns=['reading score','writing score']

    cat_columns=['gender','race/ethnicity','parental level of education','lunch','test preparation course']

    target_column='math score'

    numeric_pipeline=Pipeline(
        steps=[('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())]
    )
    cat_pipeline=Pipeline(
        steps=[('imputer',SimpleImputer(strategy='most_frequent')),('oneHotEncoder',OneHotEncoder()),('scaler',StandardScaler(with_mean=False))]
    )
    preprocessor=ColumnTransformer([('numeric_pipeline',numeric_pipeline,numeric_columns),('cat_pipeline',cat_pipeline,cat_columns)])
    ingestion()
    train_data=pd.read_csv('artifacts/train_data.csv')
    train_input=train_data.drop(target_column,axis=1)
    test_data=pd.read_csv('artifacts/test_data.csv')
    test_input=test_data.drop(target_column,axis=1)
    train_input=preprocessor.fit_transform(train_input)
    test_input=preprocessor.transform(test_input)
    train_data=np.c_[train_input,np.array(train_data[target_column])]
    test_data=np.c_[test_input,np.array(test_data[target_column])]
    file_path=os.path.join('artifacts','preprocessor.pkl')
    save_fxn(file_path,preprocessor)           

    return (train_data,test_data,file_path)   



