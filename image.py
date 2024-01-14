from PIL import Image
import os

def rotate_image(image_path, output_path, angles):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    original_image = Image.open(image_path)

    for angle in angles:
        rotated_image = original_image.rotate(angle)
        output_filename = f"{output_path}/rotated_{angle}.png"
        rotated_image.save(output_filename)
        print(f"Image saved: {output_filename}")

image_path = "/media/navnkumar/New Volume/dog.jpeg"
output_path = "/media/navnkumar/New Volume/output"
rotation_angles = [10,20,45,60,90, 180, 270]

rotate_image(image_path, output_path, rotation_angles)
