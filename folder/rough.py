import pandas as pd
import os 
import numpy as np
import matplotlib.pyplot as plt

file_name = '10009.txt'

# df = pd.read_table(file_name, low_memory=False)
# df = pd.DataFrame(df)
columns = ['time_stamp','P_EC_FAULT_STATUS','P_EC_STATUS']
df = pd.read_csv(file_name, header=None, names=columns)

print(df.head())