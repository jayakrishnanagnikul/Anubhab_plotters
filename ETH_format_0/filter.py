'''Threshold Filter
Anubhab'''

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = 10010

filename = f'{file}.txt'

df = pd.read_csv(filename, index_col=False, low_memory=False)

# print(df.head())


thresholds = {
'Time H:i:s.m' : (1712209048672600, 1712295448672600),
'P_CDT_Time' : (-1074868152, 2146357320),
'P_IMUR_X_M' : (-400, 400),
'P_IMUR_Y_M' : (-400, 400),
'P_IMUR_Z_M' : (-400, 400),
'P_IMUA_X_M' : (-300, 300),
'P_IMUA_Y_M' : (-300, 300),
'P_IMUA_Z_M' : (-300, 300),
'P_IMU_STATUS_M' : (-1000, 100),
'P_IMU_datagram_counter' : (-1000, 100),
'P_numOfDataInvalID' : (-10000, 10000),
'P_IMU_proc_delta_packet_count' : (-1000, 100),
'P_IMUT_GYRO_Y ' : (-45, 85),
}


columns_data = df.values.T.tolist()

# P_CDT_Time column data
x_data = df['P_CDT_Time']
temp_data = []
valid_data = []
valid_indices = []
valid_data.append(x_data[0])
valid_indices.append(0)

diff = 100000

temp = x_data[0]

for i in range(1,len(x_data)):
    if (x_data[i] > (temp + diff)) or (x_data[i] < temp):
        continue
    else:
        valid_data.append(x_data[i])
        valid_indices.append(i)
        temp = x_data[i]


# plt.plot(valid_data)
# plt.grid(True)
# plt.show()

# Create a directory to save plots if it doesn't exist
output_directory = f'{file}'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


for column_name in df.columns:
    if column_name == 'P_CDT_Time':
        continue  
    column_data = df[column_name][valid_indices]
    
    column_data = column_data.dropna()
    
    # thresholds
    min_threshold, max_threshold = thresholds.get(column_name, (None, None))
    if min_threshold is not None and max_threshold is not None:
        column_data = column_data.apply(lambda value: value if min_threshold <= value <= max_threshold else None)

    plt.plot(valid_data, column_data, label=column_name)

    plt.title(column_name)
    plt.xlabel('CDT Time')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    # Save plot 
    plot_filename = os.path.join(output_directory, f'{column_name}_plot.png')
    plt.savefig(plot_filename)
    # plt.show()
    plt.close() 