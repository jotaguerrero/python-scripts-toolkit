## Requirements

In order to use the script you'll need to install some libraries. You'll find them in the `requirements.txt` file that you can install with the command `pip install -r requirements.txt`. In order to run the scripts that uses the tkinter library you need to have it previously installed in your system, you can do so by running these commands:

### Mac OS

- `brew install python-tk`

### For Debian-based Linux:

- `sudo apt install python-tk`

### For Arch-based Linux:

- `sudo pacman -S tk`

### Windows:

- If you installed the `requirements.txt` file, the tk library should be enough to run the scripts

## [Drop 'N' Save Duplicates](drop-n-save-duplicates.py)

- Run the script and a window will pop up (python3 drop-n-save-duplicates.py)
- Enter the column to compare and drop duplicates
- Select the CSV file
- The script will automatically and it'll save a duplicates.csv file containing duplicated values and a unique.csv file with all unique values

## [Merge CSV Files](merge-csv.py)

- Run the script and a window will pop up (python3 merge-csv.py)
- Make sure all .csv files have the same column names
- Select the directory containing all the .csv files
- The script will automatically and merge all .csv files into a single DataFrame
- The user will be prompted to select a file name and directory to save the merged DataFrame

## [Merge Excel Files](merge-excel.py)

- Run the script and a window will pop up (python3 merge-excel.py)
- Make sure all .xlsx files have the same column names
- Select the directory containing all the .xlsx files
- The script will automatically and merge all .xlsx files into a single DataFrame
- The user will be prompted to select a file name and directory to save the merged DataFrame

## [Query a CSV file using SQL Syntax](query-csv-gui.py)

- Run the script and a window will pop up (python3 query-csv.py)
- Select up to two .csv files as DataFrames to query from (named database1 and database2 respectively)
- Write your query in the text box using SQL syntax
- Press the "Run Query" button and the output will appear in the terminal
- The user will be prompted to select a file name and directory to save the output as a .csv file

## [Query a CSV file using SQL Syntax (just in case the 'gui' version doesn't work)](query-csv.py)

- Run the script and a window will pop up (python3 query-csv.py)
- Select up to two .csv files as DataFrames to query from (named database1 and database2 respectively)
- Modify the query inside the code before executing
- The user will be prompted to select a file name and directory to save the output as a .csv file
- Results will be also printed to the terminal
