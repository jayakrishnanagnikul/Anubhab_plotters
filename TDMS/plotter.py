import pandas as pd
from nptdms import TdmsFile
import plotly.graph_objs as go
import os

file_names = [f for f in os.listdir() if f.endswith('tdms')]

# file1 = 'VP-003 ACC POST Z-AXIS_2023_Oct_03_17h_13m_20Sec.tdms'
# print(file_names)


for file in file_names:
    tdms_file = TdmsFile(file)

    file1_data = pd.DataFrame()

    for group in tdms_file.groups():
        df = group.as_dataframe()
        if(len(df.columns.to_list())>1):
            file1_data = df


    print(file1_data.head())

    file1_data['AITime'] = pd.to_datetime(file1_data['AITime'], format='%Y/%m/%d %H:%M:%S.%f')

    file1_data['AITime'] = (file1_data['AITime'] - file1_data['AITime'][0]).dt.total_seconds()


    # Convert datetime columns to consistent datetime format
    file1_data['AITime'] = pd.to_timedelta(file1_data['AITime'], unit='us')

    # print(file1_data['AITime'])


    # Define columns to plot
    columns_to_plot_file1 = [col for col in file1_data.columns if (col!='AITime')]  # Adjust these columns based on your file1

    # Create traces for each column in both datasets
    traces_file1 = []

    for col in columns_to_plot_file1:
        trace = go.Scatter(x=file1_data['AITime'], y=file1_data[col], mode='lines', name=f'{col}')
        traces_file1.append(trace)



    # Create layout
    layout = go.Layout(title=f'{file}',
                    xaxis=dict(title='Time(us)'),
                    yaxis=dict(title='Value'))


    # Create figure and add traces
    fig = go.Figure(data=traces_file1, layout=layout)

    figname = f'{file}.html'
    fig.write_html(figname, auto_open=True)

