# basic image processing tasks, such as resizing or applying filters. using python

from PIL import Image, ImageFilter

# Open an image file
input_image_path = "wall55.jpg"
output_image_path = "output_image1.jpg"
image = Image.open(input_image_path)

# Display the original image
image.show()

# Resize the image
new_size = (100,200)
resized_image = image.resize(new_size)
resized_image.show()

# Apply a filter (blur in this case)
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# Save the processed images
resized_image.save("resized_image.jpg")
blurred_image.save("blurred_image.jpg")
