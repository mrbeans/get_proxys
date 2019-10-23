# from tesserocr import PyTessBaseAPI

# images = ['1-26.jpg','Unknown.png','8080.gif']

# # with PyTessBaseAPI() as api:
# #     for img in images:
# #         api.SetImageFile(img)
# #         print(api.GetUTF8Text())

# import sys
# from pytesseract import *
# import requests
# import os
# import re
# from PIL import Image
# from PIL import ImageEnhance
# import pkg_resources
# import pdb

# for root, dirs, files in os.walk('img',followlinks=True):
#     for file in files:
#         print('now process file:{0}'.format(file))
#         if(file[-3:]=='gif'):
#             print('1111')
#             image = Image.open('{root}/{file}'.format(root=root,file=file))
#             image = image.convert('L')
#             threshold = 250 
#             initTable = lambda x:0 if x < threshold else 1
#             binaryImage = image.point(initTable, '1')
#             vcode = image_to_string(binaryImage, lang="eng", config='--psm 11')
#             print(vcode)
#             print(type(vcode))
#         else:
#             with PyTessBaseAPI() as api:
#                 api.SetImageFile('{root}/{file}'.format(root=root,file=file))
#                 print(api.GetUTF8Text())

from aip import AipOcr
import os

APP_ID = '16972495'
API_KEY = 'uH6uZALxWbwQ39VBiESUQ7yC'
SECRET_KEY = 'PgIFLjOXGiI0gOjQMgSNB97wKjgOvOdA'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

for root, dirs, files in os.walk('img',followlinks=True):
    for file in files:
        img_path='{root}/{file}'.format(root=root,file=file)
        print('------------'+img_path)
        with open(img_path, 'rb') as fp:
            """ 调用通用文字识别, 图片参数为本地图片 """
            a=client.numbers(fp.read());
            print(a)

            """ 如果有可选参数 """
            options = {}
            # options["language_type"] = "CHN_ENG"
            options["detect_direction"] = "true"
            options["detect_language"] = "true"
            options["probability"] = "true"

            """ 带参数调用通用文字识别, 图片参数为本地图片 """
            b=client.numbers(fp.read(), options)
            print(b)
