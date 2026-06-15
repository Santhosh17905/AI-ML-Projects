try:
    from PIL import Image
except ImportError:
    import Image
    

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

info = recText('C:/Users/SANTHOSH/Downloads/AI-ML-Projects/Day_17/code/TEST2.jpg')
print(info)



file = open("New.txt","a")
file.write(info)
file.close()
print("Written Successful")
