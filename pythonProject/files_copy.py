import os
import shutil
from pathlib import Path

source = os.listdir("source_path")
destination = "destination_path"


for folder in source:
    file = Path(os.path.join("source_path", folder, "main.cpp"))
    if file.is_file():
        os.mkdir(os.path.join(destination, folder))
        shutil.copy(file, os.path.join(destination, folder))
