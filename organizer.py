import os

# Path to Downloads folder
DOWNLOADS_PATH = r"C:\Users\LENOVO\Downloads"

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".cpp", ".ipynb"]
}

def create_folders():
    """Create category folders if they don't already exist."""
    for folder in FILE_TYPES.keys():
        os.makedirs(os.path.join(DOWNLOADS_PATH, folder), exist_ok=True)
    os.makedirs(os.path.join(DOWNLOADS_PATH, "Others"), exist_ok=True)

def move_files():
    """Move files into their categorized folders."""
    for file in os.listdir(DOWNLOADS_PATH):
        file_path = os.path.join(DOWNLOADS_PATH, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        ext = ext.lower()
        moved = False

        # Check category
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                destination = os.path.join(DOWNLOADS_PATH, folder, file)
                os.rename(file_path, destination)
                print(f"Moved {file} → {folder}")
                moved = True
                break

        # Unknown extension
        if not moved:
            destination = os.path.join(DOWNLOADS_PATH, "Others", file)
            os.rename(file_path, destination)
            print(f"Moved {file} → Others")

if __name__ == "__main__":
    create_folders()
    move_files()
    print("\n File organization complete!")



