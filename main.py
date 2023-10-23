from pathlib import Path
from typing import List
import shutil

CATEGORY_MAP = {
    'jpg': 'Pictures', 'jpeg': 'Pictures', 'png': 'Pictures',
    'mp3': 'Audio', 'flac': 'Audio',
    'mp4': 'Video', 'mkv': 'Video',
    'pdf': 'Documents', 'doc': 'Documents',
    'xls': 'Spreadsheets', 'xlsx': 'Spreadsheets',
    'ppt': 'Presentations', 'pptx': 'Presentations',
    'py': 'Code', 'js': 'Code',
    'zip': 'Compressed', 'rar': 'Compressed',
    'iso': 'Disk_Images', 'dmg': 'Disk_Images',
    '': 'Unknown'
}


def get_files_in_directory(directory: Path) -> List[str]:
    return [f.name for f in directory.iterdir() if f.is_file()]


def ensure_directory_exists(directory: Path):
    if not directory.exists():
        directory.mkdir()


def move_file(src: Path, dest: Path):
    counter = 1
    while dest.exists():
        dest = dest.with_stem(f"{dest.stem}_{counter}")
        counter += 1
    shutil.move(src, dest)


def move_files_to_folders(files: List[str], src_directory: Path):
    for i, file in enumerate(files, 1):
        src_path = src_directory / file
        file_extension = src_path.suffix[1:]

        category = CATEGORY_MAP.get(file_extension, 'unknown')
        folder_path = src_directory / category

        ensure_directory_exists(folder_path)

        dest_path = folder_path / file
        move_file(src_path, dest_path)
        print(f"{i}. {src_path} >>> {dest_path}")


def get_downloads_folder() -> Path:
    return Path.home() / 'Downloads'


if __name__ == "__main__":
    downloads_path = get_downloads_folder()
    files = get_files_in_directory(downloads_path)
    move_files_to_folders(files, downloads_path)
