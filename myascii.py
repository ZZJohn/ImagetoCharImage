from PIL import Image
import argparse

def get_char(r, g, b, alpha=255):
    if alpha==0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    unit = (256.0+1)/length
    return ascii_char[int(gray/unit)] #when gray=255, int(gray/unit) should be 69

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-w', '--width', type=int, default=100)
parser.add_argument('-o', '--output')
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
OUTPUT = args.output
'''
IMG = "011.png"
WIDTH = 100
OUTPUT = None
'''
#the char becomes more and more like whitespace as the index increases
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
im = Image.open(IMG)
width, height = im.size
im = im.resize((WIDTH, int(WIDTH*height/width)))
WIDTH, HEIGHT = im.size
txt = ""
for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j, i)))
    txt += '\n'
print txt
if OUTPUT:
    with open(OUTPUT, "w") as f:
        f.write(txt)
else:
    with open("output.txt", "w") as f:
        f.write(txt)