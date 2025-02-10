import os
from PIL import Image

currdir = os.getcwd()
webp_files = [file for file in os.listdir(currdir) if file.endswith(".webp")]

if not webp_files:
    print("no .webp files found")
else:
    for file in webp_files:
        file_path = os.path.join(currdir, file)
        img = Image.open(file_path)
        img.save(file_path.replace(".webp", ".png"), "PNG")
        os.remove(file_path)
        
    print("All .webp files converted to .png (.webp files deleted)")