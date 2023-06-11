import pandas as pd
import duckdb
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Define the window / font theme colors
bg_color = "#333333"
fg_color = "#FFFFFF"
text_bg_color = "#202020"
text_fg_color = "#FFFFFF"

def select_file(file_label):
    # Open a dialog box to select the CSV file
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))
    if file_path:
        file_label.config(text=file_path)

def run_query():
    # Read the CSV files with pandas to set the DataFrame to query from
    file_path1 = file_label1.cget("text")
    database1 = pd.read_csv(file_path1) if file_path1 else None
    # [Optional] Read a second CSV file and join the resulting DataFrames in the query box
    file_path2 = file_label2.cget("text")
    database2 = pd.read_csv(file_path2) if file_path2 else None

    # Get the query from the text box
    query = query_text.get("1.0", tk.END).strip()

    # Execute the query
    if database1 is not None:
        df = duckdb.query(query).df()
    else:
        df = duckdb.query(query, database1=database1, database2=database2).df()

    # Save the output to a new CSV file
    save_path = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", filetypes=(("CSV files", "*.csv"),))
    if save_path:
        df.to_csv(save_path, index=False)

    # Print the resulting DataFrame from the query
    print(df)

# Create the main window
root = tk.Tk()
root.title("📊 CSV Query Tool 🛠️")

# Configure padding
root.configure(padx=20, pady=20)

# Set the window background color
root.configure(background=bg_color)

# Create a frame for the file selection
file_frame1 = ttk.Frame(root)
file_frame1.pack(pady=10)

# Set the frame background color
file_frame1.configure(style="FileFrame.TFrame")

# Create file selection objects
file_label1 = ttk.Label(file_frame1, text="", foreground=fg_color, background=bg_color)
file_label1.pack(side="left", padx=10)

select_button1 = ttk.Button(file_frame1, text="Select File (database1)", command=lambda: select_file(file_label1))
select_button1.pack(side="left")

clear_button1 = ttk.Button(file_frame1, text="Clear File", command=lambda: file_label1.config(text=""))
clear_button1.pack(side="left", padx=10)

# Create a frame for the optional second file selection
file_frame2 = ttk.Frame(root)
file_frame2.pack(pady=10)

# Set the frame background color
file_frame2.configure(style="FileFrame.TFrame")

# Create file selection objects
file_label2 = ttk.Label(file_frame2, text="", foreground=fg_color, background=bg_color)
file_label2.pack(side="left", padx=10)

select_button2 = ttk.Button(file_frame2, text="Select File (database2)", command=lambda: select_file(file_label2))
select_button2.pack(side="left")

clear_button2 = ttk.Button(file_frame2, text="Clear File", command=lambda: file_label2.config(text=""))
clear_button2.pack(side="left", padx=10)

# Create a frame for the query input
query_frame = ttk.Frame(root)
query_frame.pack(pady=10)

# Set the frame background color
query_frame.configure(style="QueryFrame.TFrame")

# Create a label and text box for the query
query_label = ttk.Label(query_frame, text="Write your query:\n", foreground=fg_color, background=bg_color)
query_label.pack()

query_text = tk.Text(query_frame, height=15, width=70, bg=text_bg_color, fg=text_fg_color,  insertbackground=fg_color)
query_text.pack()

# Set the query sample
query_sample = "SELECT *\nFROM database1\n"
query_text.insert("1.0", query_sample)

# Create a button to run the query
run_button = ttk.Button(root, text="Run Query", command=run_query)
run_button.pack(pady=10)

# Apply styles
style = ttk.Style()

style.configure("TFrame", background=bg_color)
style.configure("TLabel", foreground=fg_color, background=bg_color)
style.configure("TButton", foreground=fg_color, background=bg_color, padx=5, pady=5)

style.configure("FileFrame.TFrame", background=bg_color)
style.configure("QueryFrame.TFrame", background=bg_color)

# Start the main event loop
root.mainloop()