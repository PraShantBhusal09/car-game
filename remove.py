from rembg import remove
from PIL import Image
import io

# Load the image (replace the path with your image file)
input_path = r"C:\Users\ACER\Desktop\thapathali.jpg"  # Use the correct image path

# Read the image into memory
with open(input_path, 'rb') as input_file:
    input_data = input_file.read()

# Remove the background
output_data = remove(input_data)

# Convert the output binary data to an image
output_image = Image.open(io.BytesIO(output_data))

# To simulate a top view, we can rotate the image 90 degrees to align it like a top view
output_image = output_image.rotate(225, resample=Image.BICUBIC, expand=True)

# Save the output image (without background)
output_image.save('output_image_top_view.png')  # This saves the image as PNG (with transparency)

# Show the result
output_image.show()
