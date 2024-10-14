# Faculty Information Viewer
Faculty Information Viewer is a Python-based tool that allows users to extract and display faculty information from HTML files. The tool provides a user-friendly interface using Tkinter, where users can select a faculty member from a drop-down menu and view their details. It also generates a .txt file with the extracted information for each selected faculty member.
## Features
- Select Faculty Member: Choose from a list of faculty members (HTML files) via a drop-down menu.
- Display Information: View extracted faculty details, including name, title, department, office, phone number, and email.
- Generate Text File: Automatically save the extracted information to a .txt file.
## Technologies Used
- Python 3.11.9
- Tkinter for the graphical user interface (GUI)
- Regular Expressions for HTML parsing
- OS Module for cross-platform path handling
## Installation
1. Download the repository / Clone the repository from GitHub.
2. Navigate to the project folder.
3. Install required packages: Tkinter is included with most Python installations. You can install Tkinter using: pip install tk
4. Ensure the Faculty folder is populated with the HTML files that contain the faculty member information.
## Running the Project
1. In the main project directory, run: python faculty_viewer.py
2. Select a faculty member from the drop-down menu.
3. View the extracted information in a pop-up window and a .md file will be saved with the same name as the HTML file.
4. Optional: To fetch all data at once in .txt files, run: python main.py
## File Structure
### FLProj/
- Faculty/                # Folder containing HTML files for faculty members
- faculty_viewer.py       # Main Python script with GUI
- main.py                 # Script to fetch and save all data at once
- README.md               # Project documentation
- requirements.txt        # Optional: Include if there are specific requirements
