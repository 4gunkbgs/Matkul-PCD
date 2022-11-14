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
        'RGB', (int(img_input.size[0]/scale), int(img_input.size[1]/scale)))
    pixels = img_output.load()
    pixels_input = img_input.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = pixels_input[i*scale, j*scale]
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
            if i < img_input.size[0]/2 and j < img_input.size[1]/2:
                r, g, b = img_input.getpixel((i, j))
                r2, g2, b2 = img_input2.getpixel((i, j))
                r_blend = int(0.5*r + (1-0.5)*r2)
                g_blend = int(0.5*g + (1-0.5)*g2)
                b_blend = int(0.5*b + (1-0.5)*b2)
                pixels[i, j] = (r_blend, g_blend, b_blend)
            else:
                r, g, b = img_input.getpixel((i, j))
                pixels[i, j] = (r, g, b)

    img_output = ImgBrightness(img_output, coldepth, 50)

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


def ImgShrinking2(img_input, coldepth, scale):
    if coldepth != 24:
        img_input = img_input.convert('RGB')

    pixels = img_input.load()
    horizontalSize = img_input.size[0]
    verticalSize = img_input.size[1]
    img_output = Image.new("RGB", (horizontalSize//scale, verticalSize//scale))
    newPixels = img_output.load()
    for i in range(horizontalSize//scale):
        for j in range(verticalSize//scale):
            r, g, b = pixels[i*scale, j*scale]
            newPixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


def ImgTest10(img_input, img_input2, coldepth):

    if coldepth != 25:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    # img_input_pixels = img_input.load()
    # horizontal_size = img_input.size[0]
    # vertical_size = img_input.size[1]

    # flipping image1
    img_input_flip = ImgFlippingHor(img_input, coldepth, "horizontal")
    # img_input_flip = Image.new('RGB', (img_input.size[1], img_input.size[0]))
    # pixels = img_input_flip.load()

    # for i in range(horizontal_size):
    #     for j in range(vertical_size):
    #         pixels[i, j] = img_input_pixels[horizontal_size-1-i, j]

    print(img_input)
    print(img_input2)

    # shrinking image2 & rotating image2
    img_input2_shrink = ImgShrinking(img_input2, coldepth, 4)
    img_input2_shrink = ImgRotate270(img_input2_shrink, coldepth, 270)

    # blending image1 and image2
    img_input_flip = img_input_flip.convert('RGB')
    img_input2_shrink = img_input2_shrink.convert('RGB')

    canvas = Image.new('RGB', (img_input_flip.size[0], img_input_flip.size[1]))
    canvas_pixels = canvas.load()

    print('ini size kanvas')
    print(canvas.size)

    img_input_flip_pixels = img_input_flip.load()
    img_input2_shrink_pixels = img_input2_shrink.load()

    for i in range(img_input_flip.size[0]):
        for j in range(img_input_flip.size[1]):
            if i < img_input2_shrink.size[0] and j < img_input2_shrink.size[1]:
                r, g, b = img_input_flip_pixels[i, j]
                r2, g2, b2 = img_input2_shrink_pixels[i, j]
                # canvas_pixels[i, j] = (r//2+r2//2, g//2+g2//2, b//2+b2//2)
                r_blend = int(0.5*r + (1-0.5)*r2)
                g_blend = int(0.5*g + (1-0.5)*g2)
                b_blend = int(0.5*b + (1-0.5)*b2)
                canvas_pixels[i, j] = (r_blend, g_blend, b_blend)
            else:
                r, g, b = img_input_flip_pixels[i, j]
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

    img_input2_shrink = img_input2_shrink.convert('RGB')

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

    # #solusi 1
    # for i in range(img_output.size[0]):
    #     for j in range(img_output.size[1]):
    #         r, g, b = img_input.getpixel((i, j))
    #         if i < img_output.size[0]/2 and j < img_output.size[1]/2:
    #             if i <= j:
    #                 pixels[i, j] = (255-r, 255-g, 255-b)
    #             else:
    #                 pixels[i, j] = (r, g, b)
    #         if i >= img_output.size[0]/2 and j < img_output.size[1]/2:
    #             if i-img_output.size[0]/2+j < img_output.size[1]/2:
    #                 pixels[i, j] = (r, g, b)
    #             else:
    #                 pixels[i, j] = (255-r, 255-g, 255-b)
    #         if i < img_output.size[0]/2 and j >= img_output.size[1]/2:
    #             if i+(j-img_output.size[1]/2) < img_output.size[0]/2:
    #                 pixels[i, j] = (255-r, 255-g, 255-b)
    #             else:
    #                 pixels[i, j] = (r, g, b)
    #         if i >= img_output.size[0]/2 and j >= img_output.size[1]/2:
    #             if i >= j:
    #                 pixels[i, j] = (255-r, 255-g, 255-b)
    #             else:
    #                 pixels[i, j] = (r, g, b)

    # solusi 2
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if i <= j:
                if i+j < img_output.size[1]:
                    pixels[i, j] = (255-r, 255-g, 255-b)
                else:
                    pixels[i, j] = (r, g, b)
            else:
                if i+j < img_output.size[0]:
                    pixels[i, j] = (r, g, b)
                else:
                    pixels[i, j] = (255-r, 255-g, 255-b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

# slicing image into 4 parts


def ImgTest13(img_input, coldepth):

    if coldepth != 25:
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
            if i < img_output.size[0]/2:
                canvas_pixels[i, j] = (r, g, b)
            canvas_pixels[i+img_input.size[0]/2, j] = (r, g, b)
            canvas_pixels[i, j+img_input.size[1]/2] = (r, g, b)
            canvas_pixels[i+img_input.size[0]/2,
                          j+img_input.size[1]/2] = (r, g, b)

            # if i < img_output.size[0]/2:
            #     if j < int(img_output.size[1]/2):
            #         if j < int(img_output.size[1]/4):
            #             gray = (r+g+b)//3
            #             pixels[i, j] = (gray, gray, gray)
            #         else:
            #             pixels[i, j] = (r, g, b)
            #     else:
            #         pixels[i, j] = (255-r, 255-g, 255-b)
            # else:
            #     if j < int(img_output.size[0]/2):
            #         pixels[i, j] = (255-r, 255-g, 255-b)
            #     else:
            #         pixels[i, j] = (r, g, b)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas

# blending 2 image with different size:


def ImgTest14(img_input, img_input2, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')
        img_input2 = img_input2.convert('RGB')

    img_input2 = ImgShrinking(img_input2, coldepth, 4)
    img_input2 = img_input2.convert('RGB')

    canvas = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    canvas_pixels = canvas.load()

    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            if i < img_input2.size[0] and j < img_input2.size[1]:
                r, g, b = img_input.getpixel((i, j))
                r2, g2, b2 = img_input2.getpixel((i, j))
                canvas_pixels[i, j] = (r2, g2, b2)

    if coldepth == 1:
        canvas = canvas.convert("1")
    elif coldepth == 8:
        canvas = canvas.convert("L")
    else:
        canvas = canvas.convert("RGB")

    return canvas


def ImgMedianFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    print(img_input.size[0])
    print(img_input.size[1])

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b, b2, b3, b4, b5, b6, b7, b8, b9]
            r_list.sort()
            g_list.sort()
            b_list.sort()
            pixels[i, j] = (r_list[4], g_list[4], b_list[4])

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgMeanFilter(img_input, coldepth):

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(1, img_input.size[0]-1):
        for j in range(1, img_input.size[1]-1):
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input.getpixel((i-1, j-1))
            r3, g3, b3 = img_input.getpixel((i-1, j))
            r4, g4, b4 = img_input.getpixel((i-1, j+1))
            r5, g5, b5 = img_input.getpixel((i, j-1))
            r6, g6, b6 = img_input.getpixel((i, j+1))
            r7, g7, b7 = img_input.getpixel((i+1, j-1))
            r8, g8, b8 = img_input.getpixel((i+1, j))
            r9, g9, b9 = img_input.getpixel((i+1, j+1))
            r_list = [r, r2, r3, r4, r5, r6, r7, r8, r9]
            g_list = [g, g2, g3, g4, g5, g6, g7, g8, g9]
            b_list = [b, b2, b3, b4, b5, b6, b7, b8, b9]
            r_mean = sum(r_list)//len(r_list)
            g_mean = sum(g_list)//len(g_list)
            b_mean = sum(b_list)//len(b_list)
            pixels[i, j] = (r_mean, g_mean, b_mean)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ImgTestFilter(img_input, coldepth, n):

    print(n)

    if coldepth != 24:
        img_input = img_input.convert('RGB')

    img_output = Image.new('RGB', (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()

    for i in range(n//2, img_input.size[0]-n//2):
        for j in range(n//2, img_input.size[1]-n//2):
            r = []
            b = []
            g = []
            for k in range(n):
                for l in range(n):
                    # creating a list of the pixels around the pixel
                    r.append(img_input.getpixel((i+k-n//2, j+l-n//2))[0])
                    g.append(img_input.getpixel((i+k-n//2, j+l-n//2))[1])
                    b.append(img_input.getpixel((i+k-n//2, j+l-n//2))[2])
            # sorting the lists
            r.sort()
            g.sort()
            b.sort()
            # finding the median of the lists
            r_med = r[len(r)//2]
            g_med = g[len(g)//2]
            b_med = b[len(b)//2]
            # setting the pixel to the median value
            pixels[i, j] = (r_med, g_med, b_med)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output
