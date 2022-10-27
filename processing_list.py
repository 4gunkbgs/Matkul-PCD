from queue import Empty
from tkinter import Canvas
from PIL import Image, ImageOps
import math


def ImgNegative(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate90(img_input, coldepth, deg):
    # solusi 1
    # img_output=img_input.rotate(deg)

    print(deg)
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if deg == 90:
                r, g, b = img_input.getpixel((j, img_output.size[0]-i-1))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate180(img_input, coldepth, deg):
    # solusi 1
    # img_output=img_input.rotate(deg)

    print(deg)
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if deg == 180:
                r, g, b = img_input.getpixel(
                    (img_output.size[1]-i-1, img_output.size[0]-j-1))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgRotate270(img_input, coldepth, deg):
    # solusi 1
    # img_output=img_input.rotate(deg)

    print(deg)
    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if deg == 270:
                r, g, b = img_input.getpixel((img_output.size[0]-j-1, i))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBrightness(img_input, coldepth, brightness):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            new_r = r+brightness
            new_g = g+brightness
            new_b = b+brightness
            # clipping
            if new_r > 255:
                new_r = 255
            elif new_r < 0:
                new_r = 0
            else:
                new_r = new_r

            if new_g > 255:
                new_g = 255
            elif new_g < 0:
                new_g = 0
            else:
                new_g = new_g

            if new_b > 255:
                new_b = 255
            elif new_b < 0:
                new_b = 0
            else:
                new_b = new_b

            pixels[i, j] = (new_r, new_g, new_b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgLogaritmic(img_input, coldepth, c):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (int(c*math.log10(1+r)),
                            int(c*math.log10(1+g)), int(c*math.log10(1+b)))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgPowerLaw(img_input, coldepth, gamma):
    # solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            # print(r)
            pixels[i, j] = (int(255*(r/255)**gamma),
                            int(255*(r/255)**gamma), int(255*(b/255)**gamma))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgThreshold(img_input, coldepth, threshold):

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if r > threshold:
                r = 255
            else:
                r = 0
            if g > threshold:
                g = 255
            else:
                g = 0
            if b > threshold:
                b = 255
            else:
                b = 0
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgBlending(img_input, img_input2, coldepth, c):
    print(int(100-c))
    # solusi1
    #img_output = Image.blend(img_input,img_input2,alpha)

    # solusi2
    if coldepth != 24:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    if c == 0:
        img_output = img_input
    elif c == 1:
        img_output = img_input2
    else:
        img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
        pixels = img_output.load()
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                r, g, b = img_input.getpixel((i, j))
                r2, g2, b2 = img_input2.getpixel((i, j))
                r_blend = int(c*r + (1-c)*r2)
                g_blend = int(c*g + (1-c)*g2)
                b_blend = int(c*b + (1-c)*b2)
                pixels[i, j] = (r_blend, g_blend, b_blend)

    return img_output


def ImgTranslasiX(img_input, coldepth, cons):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input_pixels = img_input.load()

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    # print(start_x)
    # print(start_y)

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if j+cons < img_output.size[0]:
                pixels[i, j] = img_input_pixels[i, j+cons]
            else:
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTranslasiY(img_input, coldepth, cons):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input_pixels = img_input.load()

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    # print(start_x)
    # print(start_y)

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i+cons < img_output.size[0]:
                pixels[i, j] = img_input_pixels[i+cons, j]
            else:
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTranslasiXY(img_input, coldepth, x, y):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input_pixels = img_input.load()

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    start_x = x
    start_y = y

    if x < 0:
        start_x = 0
    if y < 0:
        start_y = 0

    # print(start_x)
    # print(start_y)

    for i in range(start_x, img_input.size[0]):
        for j in range(start_y, img_input.size[1]):
            new_x = i - x
            new_y = j - y

            if(new_x >= img_input.size[0] or new_y >= img_input.size[1] or new_x < 0 or new_y < 0):
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = img_input_pixels[new_x, new_y]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingHor(img_input, coldepth, direction):

    print(direction)

    if coldepth != 25:
        img_input = img_input.convert('RGB')

    img_input_pixels = img_input.load()
    horizontal_size = img_input.size[0]
    vertical_size = img_input.size[1]

    print(horizontal_size)

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(horizontal_size):
        for j in range(vertical_size):
            if direction == "horizontal":
                pixels[i, j] = img_input_pixels[horizontal_size-1-i, j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingVer(img_input, coldepth, direction):

    if coldepth != 25:
        img_input = img_input.convert('RGB')

    img_input_pixels = img_input.load()
    horizontal_size = img_input.size[0]
    vertical_size = img_input.size[1]

    print(horizontal_size)

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(horizontal_size):
        for j in range(vertical_size):
            if direction == "vertical":
                pixels[i, j] = img_input_pixels[i, vertical_size-1-j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgFlippingHorVer(img_input, coldepth, direction):

    print(direction)

    if coldepth != 25:
        img_input = img_input.convert('RGB')

    img_input_pixels = img_input.load()
    horizontal_size = img_input.size[0]
    vertical_size = img_input.size[1]

    print(horizontal_size)

    img_output = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(horizontal_size):
        for j in range(vertical_size):
            if direction == "horizontalvertical":
                pixels[i, j] = img_input_pixels[horizontal_size -
                                                1-i, vertical_size-1-j]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgZoomIn(img_input, coldepth, scale):

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new(
        'RGB', (img_input.size[1]*scale, img_input.size[0]*scale))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i/scale, j/scale))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgShrinking(img_input, coldepth, scale):

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new(
        'RGB', (int(img_input.size[1]/scale), int(img_input.size[0]/scale)))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i*scale, j*scale))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(int(img_output.size[1])):
            if j < int(img_output.size[1]/2):
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r//3, g//3, b//3)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest2(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(int(img_output.size[1])):
            if i < int(img_output.size[0]/2):
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r//3, g//3, b//3)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest3(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i <= j:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j))
                gray = (r+g+b)//3
                pixels[i, j] = (gray, gray, gray)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest4(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if i+j < img_output.size[0]:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)
            else:
                r, g, b = img_input.getpixel((i, j))
                gray = (r+g+b)//3
                pixels[i, j] = (gray, gray, gray)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest5(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if (i-img_output.size[0]/2)**2 + (j-img_output.size[1]/2)**2 < (img_output.size[0]/2)**2:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (255-r, 255-g, 255-b)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest6(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if abs(i-img_output.size[0]/2)+abs(j-img_output.size[1]/2) < img_output.size[0]/2:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (255-r, 255-g, 255-b)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest7(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new(
        'RGB', (int(img_input.size[1]/2), int(img_input.size[0]/2)))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i*2, j*2))
            pixels[i, j] = (r, g, b)

    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_output.getpixel((i, j))
            canvas_pixels[i, j] = (r, g, b)
            canvas_pixels[img_output.size[0]*2-1-i, j] = (r, g, b)
            canvas_pixels[i, img_output.size[1]*2-1-j] = (r, g, b)
            canvas_pixels[img_output.size[0]*2-i-1,
                          img_output.size[1]*2-j-1] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return canvas

# combine 2 image with different picture size


def ImgTest8(img_input, img_input2, coldepth):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            if i < img_input2.size[0] and j < img_input2.size[1]:
                r, g, b = img_input.getpixel((i, j))
                r2, g2, b2 = img_input2.getpixel((i, j))
                r_blend = int(0.5*r + (1-0.5)*r2)
                g_blend = int(0.5*g + (1-0.5)*g2)
                b_blend = int(0.5*b + (1-0.5)*b2)
                pixels[i, j] = (r_blend, g_blend, b_blend)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTest9(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new(
        'RGB', (int(img_input.size[1]/2), int(img_input.size[0]/2)))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i*2, j*2))
            pixels[i, j] = (r, g, b)

    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_output.getpixel((i, j))
            canvas_pixels[i, j] = (r, g, b)
            canvas_pixels[img_output.size[0]*2-1-i, j] = (r, g, b)
            canvas_pixels[i, img_output.size[1]*2-1-j] = (r, g, b)
            # rotating image 90 degree clockwise
            r, g, b = img_output.getpixel((j, img_output.size[0]-i-1))
            canvas_pixels[i+img_output.size[0],
                          j+img_output.size[1]] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return canvas


def ImgTest10(img_input, img_input2, coldepth):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    print(img_input.size)
    print(img_input2.size)

    img_input_pixels = img_input.load()
    horizontal_size = img_input.size[0]
    vertical_size = img_input.size[1]

    # flipping image1
    img_input_flip = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    pixels = img_input_flip.load()

    for i in range(horizontal_size):
        for j in range(vertical_size):
            pixels[i, j] = img_input_pixels[horizontal_size-1-i, j]

    # shrinking image2 & rotating image2
    img_input2_shrink = ImgShrinking(img_input2, coldepth, 4)
    img_input2_shrink = ImgRotate270(img_input2_shrink, coldepth, 270)

    # blending image1 and image2
    canvas = Image.new('RGB', (img_input_flip.size[0], img_input_flip.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_input_flip.size[0]):
        for j in range(img_input_flip.size[1]):
            if i < img_input2_shrink.size[0] and j < img_input2_shrink.size[1]:
                r, g, b = img_input_flip.getpixel((i, j))
                r2, g2, b2 = img_input2_shrink.getpixel((i, j))
                r_blend = int(0.5*r + (1-0.5)*r2)
                g_blend = int(0.5*g + (1-0.5)*g2)
                b_blend = int(0.5*b + (1-0.5)*b2)
                canvas_pixels[i, j] = (r_blend, g_blend, b_blend)
            else:
                r, g, b = img_input_flip.getpixel((i, j))
                canvas_pixels[i, j] = (r, g, b)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas


def ImgTest11(img_input, img_input2, coldepth):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    # shrink image2 & flipping image2
    img_input2_shrink = ImgShrinking(img_input2, coldepth, 4)
    img_input2_shrink = ImgFlippingHor(
        img_input2_shrink, coldepth, "horizontal")

    # blending image1 and image2
    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            if i > img_input.size[0]/2 and j < img_input2_shrink.size[1]:
                r, g, b = img_input.getpixel((i, j))
                r2, g2, b2 = img_input2_shrink.getpixel(
                    (i-img_input.size[0]/2, j))
                r_blend = int(0.5*r + (1-0.5)*r2)
                g_blend = int(0.5*g + (1-0.5)*g2)
                b_blend = int(0.5*b + (1-0.5)*b2)
                canvas_pixels[i, j] = (r_blend, g_blend, b_blend)
            else:
                r, g, b = img_input.getpixel((i, j))
                canvas_pixels[i, j] = (r, g, b)

    # rotate 180
    canvas = ImgRotate180(canvas, coldepth, 180)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas


def ImgTest12(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))

    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i < img_output.size[0]/2 and j < img_output.size[1]/2:
                if i <= j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
            if i >= img_output.size[0]/2 and j < img_output.size[1]/2:
                if i-img_output.size[0]/2+j < img_output.size[1]/2:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = (255-r, 255-g, 255-b)
            if i < img_output.size[0]/2 and j >= img_output.size[1]/2:
                if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
            if i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
                if i >= j:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
