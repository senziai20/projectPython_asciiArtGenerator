from PIL import Image, ImageDraw, ImageFont

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

# Output text saved into project dir. 
text_file = open("Output-text.txt", "w")

# Open image inside project dir. 
img = Image.open("Input.jpg")

# For windows path use 'C:\\Windows\\Fonts\\lucon.ttf'
font_lucon = ImageFont.truetype('/home/<user>/.local/share/fonts/Lucon.ttf', 15)

# The size of an image
width, height = img.size
# Print the image size i.e. width and height, to print uncomment below
# print(width, height) 
img = img.resize((
    int(scaleFactor*width), 
    int(scaleFactor*height*(oneCharWidth/oneCharHeight))), 
    Image.NEAREST)
width, height = img.size

pix = img.load()

outputImage = Image.new(
    'RGB', 
    (oneCharWidth * width, oneCharHeight * height), 
    color = (0, 0, 0))
drw = ImageDraw.Draw(outputImage)

for i in range (height):
    for j in range (width):
        r, g, b = pix[j, i]
        # print(r)
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        drw.text(
            (j*oneCharWidth, i*oneCharHeight), 
            getChar(h), 
            font = font_lucon, 
            fill = (r, g, b))

    text_file.write('\n')
# Output art-ascii image format saved
outputImage.save('Output-image.png')    
# img.save("Output.png")  

