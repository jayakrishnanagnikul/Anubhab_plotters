run:
    put your target files ('.txt') in a folder.
    copy the 'bash.sh' & 'plotter.py' files into the same folder.
    run the 'plotter.py' program

bash.sh:
    for formatting and clean-up the data file this bash script is to be run. the script is called from the the python code it self, so no need to run it separately. 
    this script creates formatted data files with prefix "formatted + {original file name}"

plotter.py: 
    you must be having 'pandas' & 'plotly' installed. use 'pip' to install these libraries if not installed already.
    the python code runs the 'bash.sh' script to format the '.txt' files.
    then it creates an overlapping plot of all the columns wrt the first column for all the 'formatted' files using plotly & saves the plots as '.html' files 

Notes:
    If the above procedure is showing error or not producing the desired o/p, then it might be of a different format.