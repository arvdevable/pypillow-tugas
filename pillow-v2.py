from PIL import Image, ImageOps
from tkinter import Tk, filedialog
import os

# Step 1: Open file dialog
root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
)

if not file_path:
    print("No file selected.")
    exit()

img = Image.open(file_path)

# Step 2: Show filter menu
print("Choose a filter:")
print("1. Grayscale")
print("2. Sepia")
print("3. Negative")

choice = input("Enter your choice (1-3): ")

# Step 3: Apply filter
if choice == "1":
    result = img.convert("L")
    filter_name = "grayscale"
elif choice == "2":
    # Sepia filter
    sepia = ImageOps.colorize(img.convert("L"), "#704214", "#C0A080")
    result = sepia
    filter_name = "sepia"
elif choice == "3":
    result = ImageOps.invert(img.convert("RGB"))
    filter_name = "negative"
else:
    print("Invalid choice.")
    exit()

# Step 4: Show result
result.show(title=filter_name)

# Step 5: Save result
base_name = os.path.splitext(os.path.basename(file_path))[0]
output_file = f"output-{base_name}-{filter_name}.png"
result.save(output_file)

print(f"Filter applied: {filter_name}. Saved as {output_file}")
