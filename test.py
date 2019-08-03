from tesserocr import PyTessBaseAPI

images = ['1-26.jpg','Unknown.png','8080.gif']

# with PyTessBaseAPI() as api:
#     for img in images:
#         api.SetImageFile(img)
#         print(api.GetUTF8Text())

import sys
from pytesseract import *
import requests
import os
import re
from PIL import Image
from PIL import ImageEnhance
import pkg_resources

image = Image.open('8080.gif')
image = image.convert('L')
threshold = 250 
initTable = lambda x:0 if x < threshold else 1
binaryImage = image.point(initTable, '1')
vcode = image_to_string(binaryImage, lang="eng", config='-psm 7')
print vcode.encode('utf-8').replace(' ','')