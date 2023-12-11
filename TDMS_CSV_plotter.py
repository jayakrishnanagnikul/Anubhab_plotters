import pandas as pd
from nptdms import TdmsFile
import plotly.graph_objs as go

file1 = 'Aug14 package.tdms'
file2 = 'rtd mod.csv'

tdms_file = TdmsFile(file1)

file1_data = pd.DataFrame()
file2_data = pd.read_csv(file2)

for group in tdms_file.groups():
    df = group.as_dataframe()
    if(len(df.columns.to_list())>1):
        file1_data = df


file1_data['Time Stamp'] = pd.to_datetime(file1_data['Time Stamp'], format='%m/%d/%Y %H:%M:%S.%f')

file1_data['Time Stamp'] = (file1_data['Time Stamp'] - file1_data['Time Stamp'][0]).dt.total_seconds()


# Convert datetime columns to consistent datetime format
file1_data['Time Stamp'] = pd.to_timedelta(file1_data['Time Stamp'], unit='s')
file2_data['Column2'] = pd.to_timedelta(file2_data['Column2'], unit='s')


downsampling_factor = 100  # Adjust as needed
file1_data = file1_data.iloc[::downsampling_factor, :]


# Define columns to plot
columns_to_plot_file1 = [col for col in file1_data.columns if (col!='Time Stamp')]  # Adjust these columns based on your file1
columns_to_plot_file2 = [col for col in file2_data.columns if (col!='Column2')]  # Adjust these columns based on your file2

# Create traces for each column in both datasets
traces_file1 = []
traces_file2 = []

for col in columns_to_plot_file1:
    trace = go.Scatter(x=file1_data['Time Stamp'], y=file1_data[col], mode='lines', name=f'{file1}- {col}')
    traces_file1.append(trace)

for col in columns_to_plot_file2:
    trace = go.Scatter(x=file2_data['Column2'], y=file2_data[col], mode='lines', name=f'{file2} - {col}')
    traces_file2.append(trace)

# Create layout
layout = go.Layout(title='Overlapping Plots',
                   xaxis=dict(title='Time'),
                   yaxis=dict(title='Value'))

# Combine traces
all_traces = traces_file1 + traces_file2

# Create figure and add traces
fig = go.Figure(data=all_traces, layout=layout)

figname = "overlayed_plot_3.html"


fig.write_html(figname, auto_open=True)