#!/bin/sh

#
# Install the required dependencies for tesserocr
#
sudo apt-get update
sudo apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev
sudo apt-get install -y python-skimage python3-tk