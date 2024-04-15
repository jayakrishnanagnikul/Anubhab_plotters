#!/bin/bash

# Iterate through all .txt files in the current directory
for input_file in *.txt; do
  if [ -f "$input_file" ]; then
    output_file="formatted_$input_file"

#     # Remove the first 8 lines and 'D:' from the input file and store the result in a temporary file
#     tail -n +9 "$input_file" | sed -e 's/^D://' -e 's/^\t//' > temp_file

#     # Save the result to the output file
#     mv temp_file "$output_file"

      # Clean up the file by deleting the first 8 lines and removing ':D'
      sed -e 's/^D://' -e 's/^\t//' "$input_file"> temp_file
      
      # Extract words from the 7th line and format as columns
      seventh_line=$(sed -n '7p' temp_file)
      IFS=' ' read -r -a columns <<< "$seventh_line"

      # Add 'time(ms)' as the first column
      header="time(ms) ${columns[@]}"
      # header=$(echo "$header" | tr ' ' ' ')

      # Replace the contents of the file with the formatted table
      echo "$header" > "$output_file"
      tail -n +9 temp_file >> "$output_file"
      rm temp_file
    echo "Processed data from $input_file has been saved in $output_file"
  fi

done
