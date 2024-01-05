from PIL import Image
import numpy as np

# Function to read an image and convert it to a string format
def image_to_string(image_path, output_path):
    # Load the image
    img = Image.open(image_path)

    # Resize the image to 240x320
    img_resized = img.resize((320, 240))

    # Ensure the image is in RGB mode
    if img_resized.mode != 'RGB':
        img_resized = img_resized.convert('RGB')

    # Convert the image to a numpy array
    img_array = np.array(img_resized)

    # Convert the array to a 16-bit color values string format
    array_string = "uint16_t image[240][320] = {\n"
    for row in img_array:
        array_string += "    {"
        for pixel in row:
            # Convert RGB to a 16-bit value (5 bits red, 6 bits green, 5 bits blue)
            # Assuming the format is 0bRRRRRGGGGGGBBBBB
            r, g, b = pixel
            color_16bit = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)
            array_string += str(color_16bit) + ", "
        array_string = array_string[:-2] + "},\n"
    array_string = array_string[:-2] + "\n};"

    # Write the string to a text file
    with open(output_path, 'w') as file:
        file.write(array_string)

# Specify the image path and output text file path
image_path = "/Users/afa/Desktop/Projects/VGA-Pac-Man/resources/bitmap.png"  # Replace with your image path
output_path = "bitmap.txt"  # Output text file path

# Run the function
image_to_string(image_path, output_path)
