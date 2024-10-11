import re
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the folder containing all HTML files (relative to the script's directory)
folder_path = os.path.join(current_dir, 'Faculty')

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        # Open and read each HTML file
        file_path = os.path.join(folder_path, filename)
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

        # Define the output file name (based on HTML file name)
        output_filename = f"{os.path.splitext(filename)[0]}.txt"
        output_file_path = os.path.join(folder_path, output_filename)

        # Write extracted information to a .txt file
        with open(output_file_path, 'w') as output_file:
            output_file.write(f"Name: {name[0] if name else 'Not found'}\n")
            if title_department:
                title, department = title_department[0]
                output_file.write(f"Title: {title}\n")
                output_file.write(f"Department: {department}\n")
            else:
                output_file.write("Title and Department: Not found\n")
            output_file.write(f"Office: {office[0] if office else 'Not found'}\n")
            output_file.write(f"Phone: {phone[0] if phone else 'Not found'}\n")
            output_file.write(f"Email: {email[0] if email else 'Not found'}\n")

        print(f"Processed {filename}, output saved to {output_filename}")

print("All files processed.")
