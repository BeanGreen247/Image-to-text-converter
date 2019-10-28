# Image to text converter in Python
## Setup
### Install python and tesseract
```
sudo apt install python python-dev python3.6 python3.6-dev python-tk protobuf-compiler
sudo apt install python-pip python3-pip 
sudo apt-get install tesseract-*
```
### Upgrade setuptools
```
pip3 install --upgrade setuptools
```
### Install the dependencies
```
pip3 install pytesseract
pip3 install tesseract
pip3 install pillow
```
## Language
To find your needed language make sure to look here https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

## Tips on improving the output
* remove noise and useless information
* increase contract
* choose the right size
* get the best possible image quality
* higher text quality (bigger DPI like 1200 DPI)
## Usage
Download the app
```
wget https://raw.githubusercontent.com/BeanGreen247/Image-to-text-converter/master/imagetotextconversion.py
```
Launch the app
```
python3.6 imagetotextconversion.py
```
It will ask for the image file location so make sure to give the full path like shown
```
Type full path to image you want to convert to text:/home/beangreen247/Pictures/text1.png
```
Next it will ask for the language used in the document
```
Type the language of the scanned document (3 letter ID):ces
```
And lastly it will ask for the output file name
```
Type output file name:text1-vystup
```
The files name will be, in my case, text1-vystup-ces.txt

Hope you like it.
