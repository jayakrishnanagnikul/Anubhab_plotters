import pandas as pd
import numpy as np
import os
from datetime import datetime,timedelta
import matplotlib.pyplot as plt

filname = '10010.txt'

df = pd.read_csv(filname,low_memory=False, index_col=False)

# Given timestamp
timestamp_str = '2024-04-05 00:27:18.558800' #put the initial data time here
timestamp_format = '%Y-%m-%d %H:%M:%S.%f'

# Convert the timestamp string to a datetime object
timestamp = datetime.strptime(timestamp_str, timestamp_format)

# Calculate the total microseconds since the Unix epoch
epoch = datetime(1970, 1, 1)
total_microseconds = int((timestamp - epoch).total_seconds() * 1_000_000)

# Print the resulting total microseconds
print(f"Total microseconds since the Unix epoch: {total_microseconds}")

T_0 = total_microseconds

columns = df.columns.to_list()

df['count_down_time_stamp'] = df[columns[0]] - T_0
print(df.head())



'''
microseconds to date time
'''

# Given number of microseconds
microseconds = 1712276838558800

# Convert microseconds to seconds
seconds = microseconds / 1_000_000

# Create a datetime object from the epoch (January 1, 1970) and add the seconds
timestamp = epoch + timedelta(seconds=seconds)

# Print the resulting timestamp
# print(f"Timestamp: {timestamp}")


'''plot
'''
x_axis_column = 'count_down_time_stamp'
y_axis_column = columns[2]

plt.plot(df[x_axis_column], df[y_axis_column], label=y_axis_column)
plt.title(y_axis_column)
plt.xlabel('CDT Time in Microseconds')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
# plt.show()


# Save plot 
plot_filename = f'{y_axis_column}_plot.png'
plt.savefig(plot_filename)
plt.close() 