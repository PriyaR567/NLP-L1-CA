import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

text=pytesseract.image_to_string(r'C:\Users\Admin\OneDrive\Desktop\NLP\L1\maya-angelou-famous-quote.png')
print(text)

