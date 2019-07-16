
import tesserocr
from PIL import Image

image = Image.open(r'img/logo.png')   #传入你所保存的图片路径
result = tesserocr.image_to_text(image)
print(result)
