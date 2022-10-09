
# ## Langkah 1 : Mendesain layout interface

import PySimpleGUI as sg 
import os.path
from PIL import Image, ImageOps
from processing_list import *



# Kolom Area No 1: Area open folder, select image, information
file_list_column = [ 
    [ 
     sg.Text("Open Image Folder :"), 
    ], 
    [ 
     sg.In(size=(20, 1), enable_events=True, key="ImgFolder"), 
     sg.FolderBrowse(), 
    ], 
    [ 
     sg.Text("Choose an image from list :"), 
    ], 
    [ 
     sg.Listbox(values=[], enable_events=True, size=(18, 10), key="ImgList") 
    ],
    [
     sg.Text("Image Input 2:"), 
    ],
    [ 
     sg.In(size=(20, 1), enable_events=True, key="ImgSelect"), 
     sg.FileBrowse(), 
    ],
    [ 
     sg.Text("Image Information:"), 
    ], 
    [ 
     sg.Text(size=(20, 1), key="ImgSize"), 
    ], 
    [ 
     sg.Text(size=(20, 1), key="ImgColorDepth"), 
    ], 
    
]


# Kolom Area No 2: Area viewer image input 
image_viewer_column = [ 
     [sg.Text("Image Input :")], 
     [sg.Text(size=(40, 1), key="FilepathImgInput")], 
     [sg.Image(key="ImgInputViewer")], 
]


# Kolom Area No 3: Area Image info dan Tombol list of processing 
list_processing = [
    [ 
     sg.Text("List of Processing:"), 
    ], 
    [ 
     sg.Button("Image Negative", size=(20, 1), key="ImgNegative"), 
    ], 
    [ 
     sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"), 
    ], 
    [ 
     sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness"), 
    ], 
    [ 
     sg.Button("Image Logaritmic", size=(20, 1), key="ImgLogaritmic"), 
    ], 
    [ 
     sg.Button("Image Blending", size=(20, 1), key="ImgBlending"), 
    ], 
    [ 
     sg.Button("Image Power Law", size=(20, 1), key="ImgPowerLaw"), 
    ], 
    [ 
     sg.Button("Image Threshold", size=(20, 1), key="ImgThreshold"), 
    ], 
    [ 
     sg.Button("Image Translasi", size=(20, 1), key="ImgTranslasi"), 
    ], 
    [ 
     sg.Button("Image TranslasiXY", size=(20, 1), key="ImgTranslasiXY"), 
    ],
    [ 
     sg.Button("Image Flipping", size=(20, 1), key="ImgFlipping"), 
    ], 
]



# Kolom Area No 4: Area viewer image output 
image_viewer_column2 = [ 
    [sg.Text("Image Processing Output:")], 
    [sg.Text(size=(40, 1), key="ImgProcessingType")], 
    [sg.Image(key="ImgOutputViewer")], 
] 


# Gabung Full layout 
layout = [ 
    [ 
    sg.Column(file_list_column), 
    sg.VSeperator(), 
    sg.Column(image_viewer_column), 
    sg.VSeperator(), 
    sg.Column(list_processing), 
    sg.VSeperator(), 
    sg.Column(image_viewer_column2), 
    ] 
] 
window = sg.Window("Mini Image Editor", layout) 


#nama image file temporary setiap kali processing output 
filename_out = "out.png" 

# Run the Event Loop 
while True:
    event, values = window.read() 
    if event == "Exit" or event == sg.WIN_CLOSED: 
        break 
## Langkah 2 : Menampilkan list file citra pada folder yang dipilih        
    # Folder name was filled in, make a list of files in the folder 
    if event == "ImgFolder": 
        folder = values["ImgFolder"] 
        print(folder)
        
        try: 
            # Get list of files in folder 
            file_list = os.listdir(folder) 
        except: 
            file_list = [] 

        fnames = [ 
            f 
            for f in file_list 
            if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().endswith((".png", ".gif")) 
        ] 
        window["ImgList"].update(fnames)
    
    elif event == "ImgList": # A file was chosen from the listbox 
        
        try: 
            filename = os.path.join( 
                values["ImgFolder"], values["ImgList"][0] 
             )
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename) 
            window["ImgProcessingType"].update(filename) 
            window["ImgOutputViewer"].update(filename=filename) 
            img_input = Image.open(filename) 
            print(img_input)
            #img_input.show()
            
            #Size 
            img_width, img_height = img_input.size 
            window["ImgSize"].update("Image Size : "+str(img_width)+" x "+str(img_height)) 

            #Color depth 
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32} 
            coldepth = mode_to_coldepth[img_input.mode] 
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
        except:
            pass
    elif event == "ImgSelect":
        
        try:  
            filename2 = values["ImgSelect"]
            #print(filename2)
            img_input2 = Image.open(filename2)
            print(img_input2)
        except:
            pass
            
    elif event == "ImgNegative": 
 
        try: 
            window["ImgProcessingType"].update("Image Negative") 
            img_output=ImgNegative(img_input,coldepth) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    
    elif event == "ImgRotate": 
 
        try: 
            window["ImgProcessingType"].update("Image Rotate") 
            img_output=ImgRotate(img_input,coldepth,90,"C") 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
        
    elif event == "ImgBrightness": 
 
        try: 
            window["ImgProcessingType"].update("Image Brightness") 
            img_output=ImgBrightness(img_input,coldepth,100) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    
    elif event == "ImgLogaritmic": 
 
        try: 
            window["ImgProcessingType"].update("Image Logaritmic") 
            img_output=ImgLogaritmic(img_input,coldepth,100) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    
    elif event == "ImgPowerLaw": 
 
        try: 
            window["ImgProcessingType"].update("Image Power Law") 
            img_output=ImgPowerLaw(img_input,coldepth,4) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass

    elif event == "ImgThreshold": 
 
        try: 
            print("ImgThreshold")
            window["ImgProcessingType"].update("Image Threshold") 
            img_output=ImgThreshold(img_input,coldepth,127) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
        
    elif event == "ImgBlending": 
 
        try: 
            window["ImgBlending"].update("Image Blending") 
            img_output=ImgBlending(img_input,img_input2,coldepth,0.7) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
        
    elif event == "ImgTranslasiXY":     
 
        try: 
            print("ImgTranslasiXY")
            window["ImgTranslasiXY"].update("Image Translasi XY") 
            img_output=ImgTranslasiXY(img_input,coldepth,50,100) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
        
    elif event == "ImgTranslasi":    
        
        cons = 100
        sumbu = "x"
 
        try: 
            print("ImgTranslasi")
            window["ImgTranslasi"].update("Image Translasi") 
            img_output=ImgTranslasi(img_input,coldepth,cons,sumbu) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
    
    elif event == "ImgFlipping":
        
        hor = "horizontal"
        ver = "vertical"
        horver = "horizontalvertical"
        
 
        try: 
            window["ImgFlipping"].update("Image Flipping") 
            img_output=ImgFlipping(img_input,coldepth,horver) 
            img_output.save(filename_out) 
            window["ImgOutputViewer"].update(filename=filename_out) 
        except: 
            pass
window.close() 

