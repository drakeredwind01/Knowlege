import os
import tqdm
from PIL import Image
import argparse

def convert_image_to_jpg(image_path):
  """Converts an image to jpg format.

  Args:
    image_path: The path to the image file.

  Returns:
    None.
  """
  image = Image.open(image_path)
  image.save(image_path + ".jpg", "JPEG")


def convert_images_in_folder(folder_path):
  """Converts all images in a folder to jpg format.

  Args:
    folder_path: The path to the folder containing the images.

  Returns:
    None.
  """
  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith(".jpg"):
        continue

      image_path = os.path.join(root, file)
      convert_image_to_jpg(image_path)


if __name__ == "__main__":
  # Create an argument parser.
  parser = argparse.ArgumentParser()

  # Add an argument for the folder path.
  parser.add_argument("folder_path", type=str, help="The path to the folder containing the images.")

  # Parse the arguments.
  args = parser.parse_args()

  # Get the folder path.
  folder_path = args.folder_path

  # Create a tqdm progress bar.
  progress_bar = tqdm.tqdm()

  # Convert all images in the folder and its subfolders to jpg format.
  convert_images_in_folder(folder_path)

  # Close the tqdm progress bar.
  progress_bar.close()
