# image_steganography
🔐 IMAGE STEGANOGRAPHY TOOL – PYTHON | LSB ENCODING & DECODING



██╗███╗   ███╗ █████╗  ██████╗ ███████╗    ███████╗████████╗███████╗ ██████╗ 
██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔════╝╚══██╔══╝██╔════╝██╔════╝ 
██║██╔████╔██║███████║██║  ███╗█████╗      ███████╗   ██║   █████╗  ██║  ███╗
██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ╚════██║   ██║   ██╔══╝  ██║   ██║
██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ███████║   ██║   ███████╗╚██████╔╝
╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ 



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
