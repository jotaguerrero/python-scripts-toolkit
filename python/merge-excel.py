import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd

# Start tkinter
root = tk.Tk()
root.withdraw()

# Ask user to select directory containing excel (.xlsx) files
path = filedialog.askdirectory(title='Select directory containing the excel files')

# Get list of excel files in the directory
files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.xlsx')]

# Read in all excel files and concatenate into single dataframe
dfs = [pd.read_excel(f).assign(file=os.path.splitext(os.path.basename(f))[0]) for f in files]
df = pd.concat(dfs, ignore_index=True)

# Ask user to specify output file location and name
output_path = filedialog.asksaveasfilename(title='Save output file as', defaultextension='.xlsx',  initialdir=os.getcwd())

# Save concatenated dataframe to output file
df.to_excel(output_path, index=False)

# Display confirmation message to user
print(f'Output saved to {output_path}')
