import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Define the dark theme colors for the resulting window
bg_color = "#333333"
fg_color = "#FFFFFF"

def select_file():
    # Open a dialog box to select the CSV file
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
    if file_path:
        process_csv(file_path)

def process_csv(file_path):
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)

    # Prompt the user to enter the column name for finding duplicates
    column_name = input_box.get()

    # Find the duplicated values in the specified column and store them in a new dataframe
    duplicates = df[df.duplicated([column_name], keep=False)]

    # Remove the duplicates from the original dataframe
    df = df.drop_duplicates([column_name], keep=False)

    # Write the duplicated values to a new CSV file
    duplicates.to_csv('duplicates.csv', index=False)

    # Write the unique values to another CSV file
    df.to_csv('unique.csv', index=False)

# Create the main window
root = tk.Tk()
root.title("🔍️ Duplicate Finder")
root.configure(background=bg_color)

# Set the window size
window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a label and text box for the column name input
input_label = tk.Label(root, text="Enter the column name:", foreground=fg_color, background=bg_color)
input_label.pack(pady=10)

input_box = tk.Entry(root, width=30, bg=bg_color, fg=fg_color)
input_box.pack(pady=5)

# Create a button to select the CSV file
select_button = tk.Button(root, text="Select File", command=select_file, bg=bg_color, fg=fg_color)
select_button.pack(pady=10)

# Start the main event loop
root.mainloop()