import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go
from subprocess import call

call("./bash.sh",shell=True)

file_names = [f for f in os.listdir() if f.startswith('formatted')]

print(file_names)
for file in file_names:
    df = pd.read_table(file , low_memory=False)
    df = pd.DataFrame(df)
    # Create an overlapping plot using Plotly Express
    columns = df.columns.to_list()
    fig = go.Figure()
    for column in df.columns[1:]:
        fig.add_trace(go.Scatter(x=df[columns[0]], y=df[column], mode='lines', name=column))

    fig.update_layout(title="Overlapping Plot of DataFrame Columns",
                    xaxis_title=columns[0],
                    yaxis_title="measurements")
    fig.write_html(f"{file}.html")

    
    