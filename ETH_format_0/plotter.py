import os
import pandas as pd
import matplotlib.pyplot as plt

files = [i for i in range(10000,10022)]
files.append(20000)
# print(files)

for file in files:

    filename = f'{file}.txt'
    df = pd.read_csv(filename , low_memory= False)
    # print(df.head())

    columns_to_plot = df.columns.to_list()

    # Convert columns to lists
    columns_data = df.values.T.tolist()


    # Create a directory to save plots if it doesn't exist
    output_directory = f'{file}'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Plot each column
    for i, column_data in enumerate(columns_data):
        # Exclude NaN values
        column_data = [value for value in column_data if pd.notnull(value)]
        
        # Plot
        plt.plot(column_data, label=df.columns[i])

        # Set title and grid
        plt.title(df.columns[i])
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.legend()
        plt.grid(True)

        # plt.show()
        # Save plot in directory
        plot_filename = os.path.join(output_directory, f'{df.columns[i]}_plot.png')
        plt.savefig(plot_filename)
        plt.close()  # Close the plot to release memory