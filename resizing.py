import os
from PIL import Image

folder_path =r""
width = 256
height = 256

for filename in os.listdir(folder_path):
    if filename.endswith((".png",".jpg",".jpeg",".gif")):
        image_path = os.path.join(folder_path,filename)
        image = Image.open(image_path)
        resized_image = image.resize((width,height))
        resized_image.save(image_path)
        image.close()