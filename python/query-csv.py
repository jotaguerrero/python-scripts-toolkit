import pandas as pd
import duckdb
import tkinter as tk
from tkinter import filedialog

# Start tkinter
root = tk.Tk()
root.withdraw()

# Open a dialog box to select the CSV file
file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))

# Read the CSV file with pandas to set the DataFrame to query from
database = pd.read_csv(file_path)

# Enter a SQL statement
df = duckdb.query("\
    select * from database\
    limit 10;\
    ").df()

# Open a dialog box to save the output
save_path = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", filetypes=(("CSV files", "*.csv"),))

# Save the output a new CSV file
df.to_csv(save_path, index=False)

# Print the resulting DataFrame from the query
print(df)