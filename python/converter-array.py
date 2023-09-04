import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# Define the window / font theme colors
bg_color = "#333333"
fg_color = "#FFFFFF"
text_bg_color = "#202020"
text_fg_color = "#FFFFFF"

# Variables to store input and converted content
input_string = ""
converted_content = ""
conversion_mode = "comma_to_newline"  # Default mode

def convert_text():
    global input_string
    global converted_content
    global conversion_mode

    # Get the input string from the text box
    input_string = input_text_box.get("1.0", tk.END).strip()

    if conversion_mode == "comma_to_newline":
        # Example: convert from '1, 2, 3' to '1\n2\n3'
        converted_content = input_string.replace(", ", "\n")
    else:
        # Example: convert from '1\n2\n3' to '1, 2, 3'
        converted_content = input_string.replace("\n", ", ")

    # Display the converted content in the preview text box
    preview_text_box.delete("1.0", tk.END)
    preview_text_box.insert(tk.END, converted_content)

def toggle_conversion_mode():
    global conversion_mode

    if conversion_mode == "comma_to_newline":
        conversion_mode = "newline_to_comma"
        mode_label.config(text="Conversion Mode: Newline to Comma")
    else:
        conversion_mode = "comma_to_newline"
        mode_label.config(text="Conversion Mode: Comma to Newline")

def save_as_text_file():
    global converted_content

    convert_text()

    if not converted_content:
        messagebox.showinfo("Save Text File", "No converted content to save.")
        return

    # Open a dialog box to save the converted content as a text file
    file_path = filedialog.asksaveasfilename(title="Save Text File", defaultextension=".txt", filetypes=(("Text files", "*.txt"),))

    if file_path:
        try:
            with open(file_path, 'w') as text_file:
                text_file.write(converted_content)
            messagebox.showinfo("Save Text File", "The converted content has been saved as a text file.")
        except Exception as e:
            messagebox.showerror("Save Text File", f"Error saving text file: {e}")

# Create the main window
root = tk.Tk()
root.title("Text Conversion Tool")

# Configure padding
root.configure(padx=20, pady=20)

# Set the window background color
root.configure(background=bg_color)

# Create a frame for input and conversion
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Set the frame background color
input_frame.configure(style="TextFrame.TFrame")

# Create a label and text box for input
input_label = ttk.Label(input_frame, text="Enter text to convert:", foreground=fg_color, background=bg_color)
input_label.pack()

input_text_box = tk.Text(input_frame, height=5, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
input_text_box.pack()

# Create a frame for the converted content preview
preview_frame = ttk.Frame(root)
preview_frame.pack(pady=10)

# Set the frame background color
preview_frame.configure(style="TextFrame.TFrame")

# Create a label for the preview
preview_label = ttk.Label(preview_frame, text="Converted Content Preview:", foreground=fg_color, background=bg_color)
preview_label.pack()

# Create a text box to display the converted content preview
preview_text_box = tk.Text(preview_frame, height=5, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
preview_text_box.pack()

# Create buttons to convert, toggle conversion mode, and save as text file
convert_button = ttk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

toggle_button = ttk.Button(root, text="Toggle Conversion Mode", command=toggle_conversion_mode)
toggle_button.pack(pady=10)

save_button = ttk.Button(root, text="Save as Text File", command=save_as_text_file)
save_button.pack(pady=10)

# Create a label to display the current conversion mode
mode_label = ttk.Label(root, text="Conversion Mode: Comma to Newline", foreground=fg_color, background=bg_color)
mode_label.pack(pady=5)

# Apply styles
style = ttk.Style()
style.configure("TButton", foreground=fg_color, background=bg_color, padx=5, pady=5)
style.configure("TextFrame.TFrame", background=bg_color)

# Start the main event loop
root.mainloop()
