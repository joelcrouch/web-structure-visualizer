import os

# Define the structure
project_structure = {
    "web_scraper": [
        "__init__.py",
        "scraper.py",
        "field_identifier.py",
        "visualizer.py",
        "search.py",
        "utils.py",
    ],
    "tests": [
        "test_scraper.py",
        "test_field_identifier.py",
        "test_visualizer.py",
    ],
}

# Create folders and files
def create_project_structure(base_dir, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            open(file_path, "w").close()  # Create empty file

# Create root files
root_files = ["setup.py", "requirements.txt", "README.md", ".gitignore", "LICENSE"]
def create_root_files(base_dir, files):
    for file in files:
        open(os.path.join(base_dir, file), "w").close()

# Run the script
base_directory = "web_scraper"
os.makedirs(base_directory, exist_ok=True)
create_project_structure(base_directory, project_structure)
create_root_files(base_directory, root_files)
