import os
from PIL import Image
import imageio

def convert_webp_to_png_or_mp4(input_dir):
    # List all files in the directory
    files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    for file in files:
        if file.endswith('.webp'):
            file_path = os.path.join(input_dir, file)
            output_file_path = os.path.splitext(file_path)[0]

            try:
                # Try reading the file as an image
                with Image.open(file_path) as im:
                    im.save(output_file_path + '.png')
                print(f"Converted {file} to PNG.")
            except:
                # If it's not an image, try reading it as a video
                try:
                    reader = imageio.get_reader(file_path)
                    fps = reader.get_meta_data()['fps']
                    writer = imageio.get_writer(output_file_path + '.mp4', fps=fps)
                    for im in reader:
                        writer.append_data(im)
                    writer.close()
                    print(f"Converted {file} to MP4.")
                except:
                    print(f"Failed to convert {file}. It might not be a valid webp file.")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    convert_webp_to_png_or_mp4(directory)
