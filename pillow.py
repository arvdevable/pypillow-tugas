from PIL import Image
from tkinter import Tk, filedialog
import os
from datetime import datetime

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
)

if not file_path:
    print("No file selected.")
    exit()

# get_filename
base_name = os.path.splitext(os.path.basename(file_path))[0]
today = datetime.now().strftime("%Y%m%d")
# img_open
img = Image.open(file_path)
# img_scale
width, height = img.size
scaled = img.resize((width // 2, height // 2))
# img_rotate
rotated = scaled.rotate(90, expand=True)
# img_gs
grayscale = rotated.convert("L")
# img_bin
threshold = 128
bw = grayscale.point(lambda x: 255 if x > threshold else 0, "1")
gray_filename = f"output-{base_name}-grayscale-{today}.png"
bw_filename   = f"output-{base_name}-bw-{today}.png"
# save
grayscale.save(gray_filename)
bw.save(bw_filename)

print(f"Processing done. Files saved as '{gray_filename}' and '{bw_filename}'")
print("Learn more: https://github.com/arvdevable/pypillow-tugas/tree/main")
