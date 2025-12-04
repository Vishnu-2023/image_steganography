from  PIL import image
import numpy as np
import matplotlib.pyplot as plt
from ipython.display import display
import ipywidgets as widgets

def texttobin(text):
    return ''.join (format(ord(i),'08b') for i in text)
    
def bintotext(bin):
    return ''.join (chr(int(binary[i:i+8],2),'08b') for i in range(0,len(binary),8))

def encodeimage(imagepath,secret_text,outputpath):
    img = Image.open(imagepath)
    img = img.convert('rgb')
    pixels = np.array(img)
    binary_secret_text = texttobin(secret_text)+'1111111111111110'
    if len(binary_secret_text)>pixels.size:
        raise ValueError    