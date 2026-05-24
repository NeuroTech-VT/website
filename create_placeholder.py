from PIL import Image
import os

# Source image path
source_image_path = r"E:\Andreid\Projects and studies\SCHOOL\3rd year spring\NeurotechAtVT\__MAIN_WORKSPACE\website\group_photo_hero_cropped.png"

# Output placeholder image path
output_placeholder_path = r"E:\Andreid\Projects and studies\SCHOOL\3rd year spring\NeurotechAtVT\__MAIN_WORKSPACE\website\placeholder_green.png"

def create_green_placeholder(src_path, dst_path):
    if not os.path.exists(src_path):
        print(f"Error: Source image not found at {src_path}")
        return

    try:
        with Image.open(src_path) as img:
            width, height = img.size
            print(f"Original size: {width}x{height}")

            # Create a new green image with the same size
            # RGB (0, 255, 0) is pure green
            placeholder = Image.new("RGB", (width, height), (0, 255, 0))
            
            # Save the placeholder
            placeholder.save(dst_path)
            print(f"Success: Placeholder created at {dst_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_green_placeholder(source_image_path, output_placeholder_path)
