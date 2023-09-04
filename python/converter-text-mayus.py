import tkinter as tk
from tkinter import ttk

# Define the window / font theme colors
bg_color = "#333333"
fg_color = "#FFFFFF"
text_bg_color = "#202020"
text_fg_color = "#FFFFFF"

def convert_to_lowercase():
    # Get the input text from the text box
    input_text = input_text_box.get("1.0", tk.END)

    # Convert the input text to lowercase
    output_text = input_text.lower()

    # Display the converted text in the output text box
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, output_text)

def convert_to_uppercase():
    # Get the input text from the text box
    input_text = input_text_box.get("1.0", tk.END)

    # Convert the input text to uppercase
    output_text = input_text.upper()

    # Display the converted text in the output text box
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, output_text)

# Create the main window
root = tk.Tk()
root.title("Text Case Converter")

# Configure padding
root.configure(padx=20, pady=20)

# Set the window background color
root.configure(background=bg_color)

# Create a frame for the input text
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Set the frame background color
input_frame.configure(style="TextFrame.TFrame")

# Create a label and text box for the input text
input_label = ttk.Label(input_frame, text="Enter your text:\n", foreground=fg_color, background=bg_color)
input_label.pack()

input_text_box = tk.Text(input_frame, height=10, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
input_text_box.pack()

# Create buttons to convert the text to lowercase and uppercase
convert_to_lowercase_button = ttk.Button(root, text="Convert to Lowercase", command=convert_to_lowercase)
convert_to_lowercase_button.pack(pady=10)

convert_to_uppercase_button = ttk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_to_uppercase_button.pack(pady=10)

# Create a frame for the output text
output_frame = ttk.Frame(root)
output_frame.pack(pady=10)

# Set the frame background color
output_frame.configure(style="TextFrame.TFrame")

# Create a label and text box for the output text
output_label = ttk.Label(output_frame, text="Converted text:\n", foreground=fg_color, background=bg_color)
output_label.pack()

output_text_box = tk.Text(output_frame, height=10, width=70, bg=text_bg_color, fg=text_fg_color, insertbackground=fg_color)
output_text_box.pack()

# Apply styles
style = ttk.Style()
style.configure("TFrame", background=bg_color)
style.configure("TLabel", foreground=fg_color, background=bg_color)
style.configure("TButton", foreground=fg_color, background=bg_color, padx=5, pady=5)
style.configure("TextFrame.TFrame", background=bg_color)

# Start the main event loop
root.mainloop()
