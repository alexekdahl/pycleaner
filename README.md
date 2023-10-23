# pycleaner

## Description
This Python script automatically organizes files in a specified directory (by default, the 'Downloads' folder) into folders based on their file types.

## Features
- Recognizes various file extensions and categorizes them.
- Creates folders if they don't exist.
- Moves files to their respective folders.
- Handles file name collisions.

## Dependencies
- Python 3.x
- pathlib
- typing
- shutil

## How to Use
1. Clone this repository or download the Python script.
2. Open a terminal window and navigate to the folder containing the script.
3. Run python <script_name>.py.

## Code Explanation
- CATEGORY_MAP: A dictionary to map file extensions to folder names.
- get_files_in_directory(directory: Path) -> List[str]: Returns a list of all the file names in the given directory.
- ensure_directory_exists(directory: Path): Checks if a directory exists, and if not, creates it.
- move_file(src: Path, dest: Path): Moves a file from src to dest, handling name collisions.
- move_files_to_folders(files: List[str], src_directory: Path): Main function to move files to folders.
- get_downloads_folder() -> Path: Returns the path to the 'Downloads' folder.
- if __name__ == "__main__": Entry point for the script.

## License
MIT License
