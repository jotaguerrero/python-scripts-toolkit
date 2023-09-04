import csv
import json
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Define the window / font theme colors
bg_color = "#333333"
fg_color = "#FFFFFF"
text_bg_color = "#202020"
text_fg_color = "#FFFFFF"

# Variables to store file paths and content
selected_file_path = ""
converted_file_content = ""

def display_selected_file_preview():
    global selected_file_path

    try:
        with open(selected_file_path, 'r') as file:
            content = file.read()
            selected_file_text.delete("1.0", tk.END)
            selected_file_text.insert(tk.END, content)
    except Exception as e:
         messagebox.showerror(f'Error reading selected file: {e}')

def convert_csv_to_json():
    global selected_file_path

    # Open a dialog box to select the CSV file
    selected_file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=(("CSV files", "*.csv"),))

    if selected_file_path:
        display_selected_file_preview()

def convert_json_to_csv():
    global selected_file_path

    # Open a dialog box to select the JSON file
    selected_file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=(("JSON files", "*.json"),))

    if selected_file_path:
        display_selected_file_preview()

def convert_and_preview():
    global selected_file_path
    global converted_file_content

    if not selected_file_path:
        messagebox.showerror('No file selected.')
        return

    # Determine the file extension for the preview box
    if selected_file_path.endswith(".csv"):
        converted_file_extension = ".json"
    elif selected_file_path.endswith(".json"):
        converted_file_extension = ".csv"
    else:
        messagebox.showerror('Unsupported file type.')
        return

    try:
        with open(selected_file_path, 'r') as file:
            content = file.read()

            if converted_file_extension == ".json":
                csv_data = list(csv.DictReader(content.splitlines()))
                converted_file_content = json.dumps(csv_data, indent=4)
            elif converted_file_extension == ".csv":
                try:
                    json_data = json.loads(content)
                    if not isinstance(json_data, list) or len(json_data) == 0 or not isinstance(json_data[0], dict):
                        raise Exception('Invalid JSON format')
                    fieldnames = json_data[0].keys()
                    output_csv = []
                    output_csv.append(",".join(fieldnames))
                    for item in json_data:
                        row = [item[field] for field in fieldnames]
                        output_csv.append(",".join(row))
                    converted_file_content = "\n".join(output_csv)
                except json.JSONDecodeError:
                    messagebox.showerror('Invalid JSON')
                    return
                except Exception as e:
                    messagebox.showerror(f'Error converting JSON to CSV: {e}')

            converted_file_preview_text.delete("1.0", tk.END)
            converted_file_preview_text.insert(tk.END, converted_file_content)
    except Exception as e:
        messagebox.showerror(f'Error converting and previewing file: {e}')

def save_converted_file():
    global selected_file_path
    global converted_file_content

    if not selected_file_path:
        messagebox.showerror('No file selected.')
        return

    if not converted_file_content:

        convert_and_preview()

    # Determine the file extension for the save dialog
    if selected_file_path.endswith(".csv"):
        file_extension = ".json"
    elif selected_file_path.endswith(".json"):
        file_extension = ".csv"
    else:
        messagebox.showerror('Unsupported file type.')
        return

    # Open a dialog box to save the converted file
    converted_file_path = filedialog.asksaveasfilename(title="Save Converted File", defaultextension=file_extension, filetypes=(("CSV files", "*.csv"), ("JSON files", "*.json")))

    if converted_file_path:
        try:
            with open(converted_file_path, 'w') as converted_file:
                converted_file.write(converted_file_content)
        except Exception as e:
            messagebox.showerror(f'Error saving converted file: {e}')


# Create the main window
root = tk.Tk()
root.title("CSV to JSON and JSON to CSV Converter")

# Configure padding
root.configure(padx=20, pady=20)

# Set the window background color
root.configure(background=bg_color)

# Create a frame for the file selection and preview
file_frame = ttk.Frame(root)
file_frame.pack(pady=10)

# Set the frame background color
file_frame.configure(style="TextFrame.TFrame")

# Create buttons to convert CSV to JSON and JSON to CSV
csv_to_json_button = ttk.Button(file_frame, text="Convert CSV to JSON", command=convert_csv_to_json)
csv_to_json_button.pack(side="left", padx=10)

json_to_csv_button = ttk.Button(file_frame, text="Convert JSON to CSV", command=convert_json_to_csv)
json_to_csv_button.pack(side="left", padx=10)

# Create a frame for the selected file preview
selected_file_frame = ttk.Frame(root)
selected_file_frame.pack(pady=10)

# Set the frame background color
selected_file_frame.configure(style="TextFrame.TFrame")

# Create a label for the selected file preview
selected_file_label = ttk.Label(selected_file_frame, text="Selected File Preview:\n", foreground=fg_color, background=bg_color)
selected_file_label.pack()

# Create a text box to display the selected file preview
selected_file_text = tk.Text(selected_file_frame, height=10, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
selected_file_text.pack()

# Create a frame for the converted file preview
converted_file_frame = ttk.Frame(root)
converted_file_frame.pack(pady=10)

# Set the frame background color
converted_file_frame.configure(style="TextFrame.TFrame")

# Create a label for the converted file preview
converted_file_label = ttk.Label(converted_file_frame, text="Converted File Preview:\n", foreground=fg_color, background=bg_color)
converted_file_label.pack()

# Create a text box to display the converted file preview
converted_file_preview_text = tk.Text(converted_file_frame, height=10, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
converted_file_preview_text.pack()

# Create buttons to convert and preview, copy to clipboard, and save
convert_and_preview_button = ttk.Button(root, text="Convert and Preview", command=convert_and_preview)
convert_and_preview_button.pack(pady=10)

save_button = ttk.Button(root, text="Save Converted File", command=save_converted_file)
save_button.pack(pady=10)

# Apply styles
style = ttk.Style()
style.configure("TButton", foreground=fg_color, background=bg_color, padx=5, pady=5)
style.configure("TextFrame.TFrame", background=bg_color)

# Start the main event loop
root.mainloop()