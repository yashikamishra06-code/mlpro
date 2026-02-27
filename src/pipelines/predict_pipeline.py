import pandas as pd
from src.utils import load_fxn
import os
def predict(gender,race,parental,lunch,course,reading,writing):
    input={
        'gender':gender,
        'race/ethnicity':race,
        'parental level of education':parental,
        'lunch':lunch,
        'test preparation course':course,
        'reading score':reading,
        'writing score':writing
    }
    input=pd.DataFrame(input,index=[0])
    preprocessor_file_path=os.path.join('artifacts','preprocessor.pkl')
    preprocessor=load_fxn(preprocessor_file_path)
    input=preprocessor.transform(input)
    model_file_path=os.path.join('artifacts','model.pkl')
    model=load_fxn(model_file_path)
    ans=model.predict(input)
    return ans