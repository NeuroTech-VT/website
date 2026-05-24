from PIL import Image
import os

image_path = r"E:\Andreid\Projects and studies\SCHOOL\3rd year spring\NeurotechAtVT\__MAIN_WORKSPACE\website\group_photo_hero_cropped.png"

if os.path.exists(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        print(f"Width: {width}, Height: {height}")
else:
    print("Image not found")
