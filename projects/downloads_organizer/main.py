from pathlib import Path

downloads_path = Path.home() / "Downloads"

print(f"Scanning folder: {downloads_path}")

for file_path in downloads_path.iterdir():
    if file_path.is_file():
        print(file_path.name, "->", file_path.suffix)