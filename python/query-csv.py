import pandas as pd
import duckdb
import tkinter as tk
from tkinter import filedialog

# Start tkinter
root = tk.Tk()
root.withdraw()

# Open a dialog box to select the CSV file
file_path1 = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
file_path2 = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))

# Read the CSV file with pandas to set the DataFrame
database1 = pd.read_csv(file_path1)
database2 = pd.read_csv(file_path2)

# Create a temporary DuckDB connection
con = duckdb.connect(database=':memory:')

# Register the DataFrames as tables in DuckDB
con.register('database1', database1)
con.register('database2', database2)

# Modify the query below as needed
query = """
SELECT *
FROM database1 a
LEFT JOIN database2 b ON a.user_id = b.user_id
LIMIT 10;
"""
df = con.execute(query).fetchdf()

# Open a dialog box to save the output
save_path = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", filetypes=(("CSV files", "*.csv"),))

# Save the output to a new CSV file
df.to_csv(save_path, index=False)

# Close the connection
con.close()

# Print the resulting DataFrame from the query
print(df)