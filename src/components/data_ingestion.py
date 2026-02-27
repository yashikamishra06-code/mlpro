import os
import pandas as pd
from sklearn.model_selection import train_test_split
def ingestion():
    folder_path=os.path.join(os.getcwd(),'artifacts')
    os.makedirs(folder_path,exist_ok=True)
    raw_data_path=os.path.join('artifacts','raw_data.csv')
    train_data_path=os.path.join('artifacts','train_data.csv')
    test_data_path=os.path.join('artifacts','test_data.csv')
    df=pd.read_csv('notebook/data.csv')
    train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
    df.to_csv(raw_data_path)
    train_set.to_csv(train_data_path)
    test_set.to_csv(test_data_path)
