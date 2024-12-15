import os
import shutil
from datetime import datetime

# Function to create a folder if it does not exist
def create_folder(destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

# Function to organize files by type
def organize_by_type(source):
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Compressed": [".zip", ".rar", ".tar", ".gz"],
        "Others": []
    }

    for file in os.listdir(source):
        full_path = os.path.join(source, file)

        if os.path.isfile(full_path):
            extension = os.path.splitext(file)[1].lower()
            folder_found = False

            for folder, extensions in file_types.items():
                if extension in extensions:
                    destination = os.path.join(source, folder)
                    create_folder(destination)
                    shutil.move(full_path, os.path.join(destination, file))
                    folder_found = True
                    break

            if not folder_found:
                destination = os.path.join(source, "Others")
                create_folder(destination)
                shutil.move(full_path, os.path.join(destination, file))

# Function to organize files by modification date
def organize_by_date(source):
    for file in os.listdir(source):
        full_path = os.path.join(source, file)

        if os.path.isfile(full_path):
            modification_date = datetime.fromtimestamp(os.path.getmtime(full_path))
            date_folder = modification_date.strftime("%Y-%m")

            destination = os.path.join(source, date_folder)
            create_folder(destination)
            shutil.move(full_path, os.path.join(destination, file))

def main():
    print("Welcome to the Intelligent File Organizer!")
    source_folder = input("Enter the path of the folder you want to organize: ")

    if not os.path.exists(source_folder):
        print("The specified folder does not exist. Please try again.")
        return

    print("Choose the organization method:")
    print("1. Organize by file type")
    print("2. Organize by modification date")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        organize_by_type(source_folder)
        print("Files successfully organized by type!")
    elif choice == "2":
        organize_by_date(source_folder)
        print("Files successfully organized by date!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
