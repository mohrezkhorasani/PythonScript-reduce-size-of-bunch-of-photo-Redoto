from PIL import Image
import os

def resize_and_compress_image(input_path, output_path, target_size_kb):
    with Image.open(input_path) as img:
        quality = 95

        while True:
            img.save(output_path, format='PNG', quality=quality)

            file_size_kb = (len(open(output_path, 'rb').read()) + 1023) // 1024
            print(f"Checking quality for {input_path}, Current Quality: {quality}, Current File Size: {file_size_kb} KB")

            if file_size_kb <= target_size_kb:
                break
            quality -= 5

            if quality < 5:
                print("Quality less than 5, breaking the loop.")
                break

def process_directory(input_directory, output_directory, target_size_kb):
    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".png"):
                input_image_path = os.path.join(root, filename)
                output_image_path = os.path.join(output_directory, os.path.relpath(input_image_path, input_directory))

                # Create the output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

                resize_and_compress_image(input_image_path, output_image_path, target_size_kb)

if __name__ == "__main__":
    input_directory = input("Please enter the INPUT directory path: ")
    output_directory = input("Please enter the OUTPUT directory path: ")
    target_size_kb = input("Please enter Target size in KB, if you want default, enter 5: ")

    process_directory(input_directory, output_directory, target_size_kb)

    print("Image compression completed. Check the output directory for the compressed images.")
