# image_steganography
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-Steganography-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

<h1 align="center">🖼️ Image Steganography – LSB Encoding & Decoding Tool</h1>

<p align="center">
  A simple and offline Python-based application to hide and extract secret messages inside images.<br>
  Built using <b>Python, PIL, NumPy, Matplotlib, and IpyWidgets</b>.
</p
🔐 IMAGE STEGANOGRAPHY TOOL – PYTHON | LSB ENCODING & DECODING

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/23d22e80-8122-4c60-a627-b2204e01ec7c" />

✨ Features

🔐 Encode text into images using LSB pixel manipulation
🔎 Decode hidden messages safely using delimiter-based extraction
🧮 Efficient image processing using NumPy
🖼 Image handling with Pillow (PIL)
🎛 Interactive UI built using ipywidgets
📊 Image preview with Matplotlib
💡 Fully offline and easy to use


🛠 Tech Stack

Python
Pillow (PIL)
NumPy
Matplotlib
IpyWidgets

📂 How It Works

1. Convert the message to binary
2. Embed bits into the LSB of RGB pixel values
3. Append a unique binary delimiter for safe extraction
4. Decode the image by scanning LSB values until the delimiter is found

▶️ Usage

Upload an image
Enter the secret message
Encode and save the modified image
Decode hidden text anytime using the provided functions


📘 Learnings
Through this project, I strengthened my skills in:
Image processing
Data encoding/decoding
UI building in Jupyter
Python automation and debugging



