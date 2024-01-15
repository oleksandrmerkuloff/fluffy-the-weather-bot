from math import ceil
from PIL import Image

# Open original image and get its size
im = Image.open('images/clouds.jpg')
w, h = im.size

# Calculate new size to comply with a 1:20 aspect ratio
newH = ceil(w/20)

# Create background of new image
padded = Image.new('RGB', (w, newH), 'magenta')

# Paste existing image into new one at vertical midpoint
padded.paste(im, (0, int((newH-h)/2)))
padded.save('result.jpg')
