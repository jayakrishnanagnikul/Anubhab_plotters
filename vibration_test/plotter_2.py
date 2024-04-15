import pandas as pd
import matplotlib.pyplot as plt
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from subprocess import call
import re

call("./script.sh",shell=True)

file_names = [f for f in os.listdir() if f.startswith('formatted')]


def count_adc_numbers(adc_list):
    # Initialize an empty set to store unique ADC numbers
    unique_adc_numbers = set()

    # Iterate through the list of strings
    for adc_string in adc_list:
        # Use regular expression to extract the ADC number from the string
        import re
        match = re.search(r'adc(\d+)', adc_string)
        
        # If a match is found, add the ADC number to the set
        if match:
            adc_number = match.group(1)
            unique_adc_numbers.add(adc_number)

    # Count the total number of different ADC numbers
    total_adc_numbers = len(unique_adc_numbers)

    return total_adc_numbers, sorted(list(unique_adc_numbers))


# print(file_names)
for file in file_names:
    df = pd.read_table(file , low_memory=False)
    df = pd.DataFrame(df)
    # Create an overlapping plot using Plotly Express
    columns = df.columns.to_list()

    adc_list = [col for col in columns if 'adc' in col]
    
    total_adc, adc_numbers = count_adc_numbers(adc_list)

    print(f'Total number of different ADC numbers: {total_adc}')
    print(f'ADC numbers present: {adc_numbers}')

    title = [f'adc{n}' for n in adc_numbers]

    fig = make_subplots(rows=total_adc, cols=1, subplot_titles=(title))
    for column in columns:
        for n in adc_numbers:
            if f'adc{n}' in column:
                fig.append_trace(go.Scatter(x=df[columns[0]], y=df[column], mode='lines', name=column), row=adc_numbers.index(n)+1, col=1)
                fig.update_xaxes(title_text = 'Time Stamp')
                fig.update_yaxes(title_text = 'Voltage')

    fig.update_layout( title_text=file[10:]) 
    # fig.show()

    fig.write_html(f"{file[10:]}.html")
    

    
    