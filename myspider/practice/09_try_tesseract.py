from PIL import Image
import pytesseract

file_path="D:\google.jpg"
img = Image.open(file_path)

#img.show()
print(pytesseract.image_to_string(img))
