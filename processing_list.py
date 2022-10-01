

from PIL import Image, ImageOps
import math


def ImgNegative(img_input,coldepth): 
    #solusi 1 
    #img_output=ImageOps.invert(img_input) 
    
    #solusi 2 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[0],img_input.size[1])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j)) 
            pixels[i,j] = (255-r, 255-g, 255-b) 

    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB") 

    return img_output


def ImgRotate(img_input,coldepth,deg,direction): 
    #solusi 1 
    img_output=img_input.rotate(deg) 

    #solusi 2 
#     if coldepth!=24: 
#         img_input = img_input.convert('RGB') 

#     img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
#     pixels = img_output.load() 
#     for i in range(img_output.size[0]): 
#         for j in range(img_output.size[1]): 
#             if direction=="C": 
#                 r, g, b = img_input.getpixel((j,img_output.size[0]-i-1)) 
#             else: 
#                 r, g, b = img_input.getpixel((img_input.size[1]-j-1,i)) 
#                 pixels[i,j] = (r, g, b)
#     if coldepth==1: 
#         img_output = img_output.convert("1") 
#     elif coldepth==8: 
#         img_output = img_output.convert("L") 
#     else: 
#         img_output = img_output.convert("RGB")
        
    return img_output

def ImgBrightness(img_input,coldepth,brightness): 
    #solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None) 

    #solusi 2 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j))
            new_r = r+brightness
            new_g = g+brightness
            new_b = b+brightness
            #clipping
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
            
            pixels[i,j] = (new_r, new_g, new_b)
            
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output

def ImgLogaritmic(img_input,coldepth,c): 
    #solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None) 

    #solusi 2 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j))
            pixels[i,j] = (int(c*math.log(1+r)), int(c*math.log(1+g)), int(c*math.log(1+b)))
            
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output

def ImgPowerLaw(img_input,coldepth,gamma): 
    #solusi 1
    #img_output=ImageOps.autocontrast(img_input, cutoff=0, ignore=None) 

    #solusi 2 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j))
            print(r)
            pixels[i,j] = (int(255*(r/255)**gamma), int(255*(r/255)**gamma), int(255*(b/255)**gamma))
            
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output

def ImgThreshold(img_input,coldepth,threshold): 

    #solusi 2 
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
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
            pixels[i,j] = (r, g, b)
            
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output

def ImgBlending(img_input,img_input2,coldepth): 
    
    #solusi1
    # img_output = Image.blend(img_input,img_input2,0.5)

    #solusi2
    if coldepth!=24: 
        img_input = img_input.convert('RGB') 
        img_input2 = img_input2.convert('RGB') 

    img_output = Image.new('RGB',(img_input.size[1],img_input.size[0])) 
    pixels = img_output.load() 
    for i in range(img_output.size[0]): 
        for j in range(img_output.size[1]): 
            r, g, b = img_input.getpixel((i, j))
            r2, g2, b2 = img_input2.getpixel((i, j))
            r_blend = r + r2
            g_blend = g + g2
            b_blend = b + b2
            pixels[i,j] = (r_blend, g_blend, b_blend)
            
            
    if coldepth==1: 
        img_output = img_output.convert("1") 
    elif coldepth==8: 
        img_output = img_output.convert("L") 
    else: 
        img_output = img_output.convert("RGB")
        
    return img_output
