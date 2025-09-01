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

# Jawaban tgs tik
print("==== JAWABAN ====")
print("1. Manfaat pengolahan gambar dengan Python:")
print("- Automasi & batch (resize, watermark, optimasi web).")
print("- Reproducible (kode bisa versi/rollback).")
print("- Integrasi pipeline (ML, web, satelit, drone).")
print("- Analisis & ekstraksi info (OCR, medis, inspeksi).")
print("- Hemat biaya (open-source).")
print("- Customisasi & eksperimen cepat.")
print("- Headless (jalan di server/container).")
print("Contoh: preprocessing citra medis, satelit, OCR arsip, e-commerce, inspeksi pabrik.\n")

print("2. Perubahan kualitas setelah resize/filter:")
print("- Resize: downscale = detail hilang; upscale = blur/pixelation.")
print("- Gunakan resampling bagus (Lanczos, bicubic) atau super-resolution.")
print("- Filter: blur kurangi noise tapi hilang tajam; sharpen buat tepi jelas tapi tambah noise.")
print("- Format: JPEG lossy; PNG lossless.")
print("Tips: simpan master asli, urutkan langkah logis (denoise→resize→sharpen→save).\n")

print("3. Kelebihan pip+Pillow vs Photoshop/GIMP:")
print("- + Automasi ribuan file dengan skrip.")
print("- + Integrasi ke server/ML pipeline.")
print("- + Gratis, ringan, open-source.")
print("- + Reproducible & bisa diuji otomatis.")
print("- - Tidak ada GUI interaktif (retouch manual susah).")
print("- - Fitur canggih Photoshop tidak ada (content-aware, CMYK).")
print("- - Butuh skill coding.")
print("Rekomendasi: pakai Python utk preprocessing & batch, Photoshop/GIMP utk editing akhir.\n")

print("NAMA KELOMPOK")
print("-Arvin")
print("-Evan")
print("-Lionel")
print("-Onza")
