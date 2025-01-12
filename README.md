
# OCR Scanner

An Optical Character Recognition (OCR) scanner built with Python that extracts text from images. This tool utilizes the Tesseract OCR engine to process and recognize text from images you upload.

## Features
- Upload images in various formats (JPEG, PNG, etc.).
- Extract text from the uploaded image using OCR.
- Display extracted text on the web interface.
  
## Prerequisites
Ensure you have the following installed:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Tesseract OCR**: [Install Tesseract](https://github.com/tesseract-ocr/tesseract)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ocr-scanner.git
   cd ocr-scanner
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install **Tesseract OCR** on your system. Follow the instructions based on your OS from the [official Tesseract page](https://github.com/tesseract-ocr/tesseract).

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and visit [http://localhost:5000](http://localhost:5000).

## Usage
- Upload an image by clicking the "Choose File" button.
- Click "Scan" to extract the text from the image.
- The extracted text will appear below the image.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
