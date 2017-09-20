# receipt-ocr
A python library to perform OCR on receipts and produce json results.

## Requirements
 * Tesseract - This project makes use of tesseract, make sure tesseract can be found on your path.
See the [included bash script](./scripts/install-dependencies.sh) for packages that can be
installed on ubuntu.
 * Pipenv - Used to package dependencies and manage virtual environments

## Getting Started
The main entrypoint for this component is ```main.py``` located within the