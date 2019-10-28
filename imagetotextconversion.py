from PIL import Image
import pytesseract

dire=input("Type full path to image you want to convert to text:")
im = Image.open(dire)

language=input("Type the language of the scanned document (3 letter ID):")
text = pytesseract.image_to_string(im, lang=language)
filename=input("Type output file name:")
file1 = open(filename+"-"+language+".txt","w")
file1.write(text)
file1.close()
print("Done...") 
