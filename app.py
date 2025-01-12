from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = None

    if request.method == 'POST':
        # Check if a file was uploaded
        if 'image' not in request.files or request.files['image'].filename == '':
            return render_template('index.html', error="Please upload an image file.")

        file = request.files['image']
        image = Image.open(file.stream)

        # Perform OCR on the uploaded image
        extracted_text = pytesseract.image_to_string(image)

    return render_template('index.html', extracted_text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)
