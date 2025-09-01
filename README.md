# Tugas II - Python Pillow

Kelompok:
- Blasius Nafiri Marvin - XI-6 - 6
- FX Evan Destama - XI-1 - 15
- Cahyo Panuluh Pepadhang Jati - XI-3 - 8
- Lionel Edward Sukamto - XI-3 - 24

## Screenshoots
<img width="1306" height="266" alt="image" src="https://github.com/user-attachments/assets/f027c2a1-d868-4176-8f31-19f0995c03d0" />
Membuka pillow.py

<img width="1240" height="788" alt="image" src="https://github.com/user-attachments/assets/513721cc-25c1-443a-9bc8-773001a0799d" />
Setelah terbuka, anda bisa memilih gambarnya sendiri di drive masing masing

> NOTE:
> Jika anda mau memilih gambar yang ada di web, anda bisa mendownload gambar tersebut dan memilihnya.

![mtwnd](https://github.com/user-attachments/assets/5ec237a4-8b59-4b86-96ea-af389a4462b5)
Saya akan memakai gambar ini sebagai contoh.

<img width="1500" height="1500" alt="output-mtwnd-grayscale-20250901" src="https://github.com/user-attachments/assets/690555d0-65de-4bc9-9935-40b8aaefa780" />
<img width="1500" height="1500" alt="output-mtwnd-bw-20250901" src="https://github.com/user-attachments/assets/789d8b33-a7cf-4c55-b31f-244f7dbe7d7e" />
Ini adalah hasil dari output program kami.

## Jawaban
### 1. Manfaat pengolahan gambar dengan Python

* Automasi & batch (resize, watermark, optimasi web).
* Reproducible (kode bisa versi/rollback).
* Integrasi pipeline (ML, web, satelit, drone).
* Analisis & ekstraksi informasi (OCR, medis, inspeksi).
* Hemat biaya (open-source).
* Customisasi & eksperimen cepat.
* Headless (jalan di server/container).

**Contoh:** preprocessing citra medis, satelit, OCR arsip, e-commerce, inspeksi pabrik.

### 2. Perubahan kualitas setelah resize/filter

* **Resize:** downscale = detail hilang; upscale = blur/pixelation.
* Gunakan resampling bagus (Lanczos, bicubic) atau super-resolution.
* **Filter:** blur mengurangi noise tapi hilang ketajaman; sharpen membuat tepi lebih jelas tapi bisa menambah noise.
* **Format:** JPEG lossy; PNG lossless.

**Tips:** simpan master asli, urutkan langkah logis (denoise → resize → sharpen → save).

### 3. Kelebihan pip+Pillow vs Photoshop/GIMP

* **Kelebihan Python (pip + Pillow):**

  * Automasi ribuan file dengan skrip.
  * Integrasi ke server/ML pipeline.
  * Gratis, ringan, open-source.
  * Reproducible & bisa diuji otomatis.

* **Kekurangan:**
  – Tidak ada GUI interaktif (retouch manual susah).
  – Fitur canggih Photoshop tidak ada (content-aware, CMYK).
  – Butuh skill coding.

**Rekomendasi:** gunakan Python untuk preprocessing & batch, lalu Photoshop/GIMP untuk editing akhir.
