from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import ipywidgets as widgets

Convert text to binary representation

def text_to_bin(text):
return ''.join(format(ord(i), '08b') for i in text)

Convert binary representation to text

def bin_to_text(binary):
return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

Encode a secret message into an image

def encode_image(image_path, secret_text, output_path):
img = Image.open(image_path)
img = img.convert('RGB')
pixels = np.array(img)

binary_secret_text = text_to_bin(secret_text) + '1111111111111110'  # Append delimiter  
  
if len(binary_secret_text) > pixels.size:  
    raise ValueError("Image is too small to hold the secret message.")  
  
data_index = 0  
for row in pixels:  
    for pixel in row:  
        for color in range(3):  # RGB channels  
            if data_index < len(binary_secret_text):  
                pixel[color] = (pixel[color] & ~1) | int(binary_secret_text[data_index])  
                data_index += 1  
  
new_img = Image.fromarray(pixels)  
new_img.save(output_path)  
print(f"Message encoded and saved to {output_path}")  
return new_img

Decode the hidden message from an image

def decode_image(image_path):
img = Image.open(image_path)
img = img.convert('RGB')
pixels = np.array(img)

binary_secret_text = ''  
for row in pixels:  
    for pixel in row:  
        for color in range(3):  # RGB channels  
            binary_secret_text += str(pixel[color] & 1)  
  
delimiter_index = binary_secret_text.find('1111111111111110')  
if delimiter_index == -1:  
    raise ValueError("No hidden message found.")  
  
binary_secret_text = binary_secret_text[:delimiter_index]  
secret_text = bin_to_text(binary_secret_text)  
  
return secret_text

Create widgets

upload_instruction = widgets.Label("1. Upload an image file to encode or decode.")
image_upload = widgets.FileUpload(accept='image/*', multiple=False)

message_instruction = widgets.Label("2. Enter the secret message (for encoding only):")
message_input = widgets.Text(placeholder='Enter your secret message here', description='Message:')

encode_button = widgets.Button(description="Encode Message")
decode_button = widgets.Button(description="Decode Message")

encoded_image_display = widgets.Output()
decoded_message_output = widgets.Output()

Define widget handlers

def on_upload_change(change):
if image_upload.value:
uploaded_file = list(image_upload.value.values())[0] if isinstance(image_upload.value, dict) else image_upload.value[0]
with open('input_image.png', 'wb') as f:
f.write(uploaded_file['content'])
upload_instruction.value = "Image uploaded successfully! You can now encode or decode the message."

def encode_and_display_image(b):
secret_message = message_input.value
if not secret_message:
encoded_image_display.clear_output()
with encoded_image_display:
print("Please enter a message to encode.")
return

try:  
    encoded_image = encode_image('input_image.png', secret_message, 'encoded_image.png')  
    encoded_image_np = np.array(encoded_image)  
      
    encoded_image_display.clear_output()  
    with encoded_image_display:  
        plt.imshow(encoded_image_np)  # Display the encoded image  
        plt.axis('off')  # Hide axes  
        plt.show()  
except Exception as e:  
    encoded_image_display.clear_output()  
    with encoded_image_display:  
        print(f"Error encoding message: {e}")

def decode_message(b):
try:
secret_message = decode_image('encoded_image.png')
decoded_message_output.clear_output()
with decoded_message_output:
print("Decoded message:", secret_message)
except Exception as e:
decoded_message_output.clear_output()
with decoded_message_output:
print(f"Error decoding message: {e}")

Set up event handlers

image_upload.observe(on_upload_change, names='value')
encode_button.on_click(encode_and_display_image)
decode_button.on_click(decode_message)

Display widgets

display(upload_instruction)
display(image_upload)
display(message_instruction)
display(message_input)
display(encode_button)
display(decode_button)
display(encoded_image_display)
display(decoded_message_output)
