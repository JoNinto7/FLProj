import os
import re
import tkinter as tk
from tkinter import ttk, messagebox

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the folder containing all HTML files (relative to the script's directory)
folder_path = os.path.join(current_dir, 'Faculty')

# Function to extract and display faculty information, and save it to a text file
def display_and_save_faculty_info(filename):
    file_path = os.path.join(folder_path, filename)
    
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"File {filename} not found!")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Step 1: Extract the Name
    name_pattern = r'<div class="name">(.*?)<\/div>'
    name = re.findall(name_pattern, html_content)

    # Step 2: Extract the Title and Department
    title_pattern = r'<div class="first-appointment">\s*(.*?)\s*&mdash;\s*(.*?)\s*<\/div>'
    title_department = re.findall(title_pattern, html_content)

    # Step 3: Extract the Office
    office_pattern = r'<div class="office">(.*?)<\/div>'
    office = re.findall(office_pattern, html_content)

    # Step 4: Extract the Phone Number
    phone_pattern = r'phone: (\(\d{3}\) \d{3}-\d{4})'
    phone = re.findall(phone_pattern, html_content)

    # Step 5: Extract the Email
    email_pattern = r'href="mailto:(.*?)"'
    email = re.findall(email_pattern, html_content)

    # Construct the result text to be shown and saved
    result_text = f"Name: {name[0] if name else 'Not found'}\n"
    if title_department:
        title, department = title_department[0]
        result_text += f"Title: {title}\n"
        result_text += f"Department: {department}\n"
    else:
        result_text += "Title and Department: Not found\n"
    result_text += f"Office: {office[0] if office else 'Not found'}\n"
    result_text += f"Phone: {phone[0] if phone else 'Not found'}\n"
    result_text += f"Email: {email[0] if email else 'Not found'}\n"
    
    # Display the result in a message box
    messagebox.showinfo("Faculty Information", result_text)

    # Save the result to a text file
    output_filename = f"{os.path.splitext(filename)[0]}.txt"
    output_file_path = os.path.join(folder_path, output_filename)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(result_text)
    
    print(f"Faculty information saved to {output_filename}")

# Function to populate the drop-down menu with HTML files
def load_files():
    files = [f for f in os.listdir(folder_path) if f.endswith(".html")]
    return files

# Tkinter window setup
root = tk.Tk()
root.title("Faculty Information Viewer")

# Label
label = ttk.Label(root, text="Select a Faculty Member:")
label.pack(padx=10, pady=10)

# Drop-down menu (Combobox)
file_combobox = ttk.Combobox(root, values=load_files())
file_combobox.pack(padx=10, pady=10)

# Button to display selected faculty info
def on_select():
    selected_file = file_combobox.get()
    if selected_file:
        display_and_save_faculty_info(selected_file)
    else:
        messagebox.showerror("Error", "Please select a faculty member.")

# Button to trigger display
button = ttk.Button(root, text="Show Info", command=on_select)
button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
