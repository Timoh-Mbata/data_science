import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine
path=r'C:\\Users\\Admin\\Desktop\\portofolio\\data_science\\databases in python\\transactions.csv'
dataset = pd.read_csv(path)
print(dataset.head(4))
engine = create_engine('postgresql://postgres:newpassword@localhost:5432/testing')

dataset.to_sql('transactions', con=engine, if_exists='append', index=False)

