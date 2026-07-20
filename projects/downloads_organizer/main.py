from pathlib import Path   

def get_category(extension,extension_map):
    return extension_map.get(extension, "Other")

extension_map = {
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.pdf': 'Documents',
    '.csv': 'Documents',
    '.xls': 'Documents',
    '.xlsx': 'Documents',
    '.pptx': 'Documents',

    '.jpg': 'Images',
    '.png': 'Images',
    '.svg': 'Images',

    '.mp4': 'Videos',
    '.mkv': 'Videos',

    '.mp3': 'Audio',
    '.flac': 'Audio',

    '.rar': 'Archives',
    '.zip': 'Archives',
    '.7z': 'Archives',

    '.exe': 'Installers',
    '.msi': 'Installers',

    '.py': 'Code',
    '.json': 'Code',
    '.yaml': 'Code',
    '.xml': 'Code'
}
downloads_path = Path.home() / "Downloads"

print(f"Scanning folder: {downloads_path}")

for file_path in downloads_path.iterdir():
    if file_path.is_file():
        category = get_category(file_path.suffix, extension_map)
        print(file_path.name, "->", category)