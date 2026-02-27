from datetime import datetime
import os
import logging

dtn=datetime.now()
file_name=f'{dtn.day}-{dtn.month}-{dtn.year}_{dtn.hour}-{dtn.minute}-{dtn.second}.log'
log_path=os.path.join(os.getcwd(),'logs')
os.makedirs(log_path,exist_ok=True)
file_path=os.path.join(log_path,file_name)

logging.basicConfig(
    filename=file_path,
    format='%(asctime)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s',
    level=logging.INFO
)