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
    [sg.HSeparator()],
    [
        sg.Text("Transformasi Aritmatika"),
    ],
    [sg.HSeparator()],
    [
        sg.Button("Image Negative", size=(12, 1), key="ImgNegative"),
        sg.Button("Image Brightness", size=(14, 1), key="ImgBrightness"),
    ],
    [
        sg.Button("Image Threshold", size=(12, 1), key="ImgThreshold"),
        sg.Button("Image Logaritmic", size=(14, 1), key="ImgLogaritmic"),
    ],
    [
        sg.Button("Image Power Law", size=(15, 1), key="ImgPowerLaw",),
        sg.Text("Nilai:"),
        sg.In(size=(5, 1), key="input1"),
    ],
    [
        sg.Button("Image Blending", size=(20, 1), key="ImgBlending"),
    ],
    [
        sg.Text("Tingkat Blending:"),
        sg.In(size=(5, 1), key="input2"),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Transformasi Geometri"),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Rotasi: "),
        sg.Button("90", size=(4, 1), key="ImgRotate90"),
        sg.Button("180", size=(4, 1), key="ImgRotate180"),
        sg.Button("270", size=(4, 1), key="ImgRotate270"),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Translasi: "),
        sg.Button("x", size=(4, 1), key="ImgTranslasiX"),
        sg.Button("y", size=(4, 1), key="ImgTranslasiY"),
        sg.Button("xy", size=(4, 1), key="ImgTranslasiXY"),
    ],
    [
        sg.Text("nilai x:"),
        sg.In(size=(5, 1), key="inputX"),
        sg.Text("nilai y:"),
        sg.In(size=(5, 1), key="inputY"),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Flipping: "),
        sg.Button("Horizontal", size=(8, 1), key="ImgFlippingHor"),
        sg.Button("Vertical", size=(8, 1), key="ImgFlippingVer"),
    ],
    [
        sg.Button("Horizontal Vertical", size=(
            15, 1), key="ImgFlippingHorVer"),
    ],
    [sg.HSeparator()],
    [
        sg.Text("Zoom: "),
        sg.Button("Zoom In", size=(8, 1), key="ImgZoomIn"),
        sg.Button("Zoom Out", size=(8, 1), key="ImgShrinking"),
    ],
    [
        sg.Text("skala:"),
        sg.In(size=(5, 1), key="skala"),
    ],
    [sg.HSeparator()],
    [
        sg.Button("Test", size=(8, 1), key="Test"),
        sg.Button("Test2", size=(8, 1), key="Test2"),
        sg.Button("Test3", size=(8, 1), key="Test3"),
    ],
    [
        sg.Button("Test4", size=(8, 1), key="Test4"),
        sg.Button("Test5", size=(8, 1), key="Test5"),
        sg.Button("Test6", size=(8, 1), key="Test6"),
    ],
    [
        sg.Button("Test7", size=(8, 1), key="Test7"),
        sg.Button("Test8", size=(8, 1), key="Test8"),
        sg.Button("Test9", size=(8, 1), key="Test9"),
    ],
    [
        sg.Button("Test10", size=(8, 1), key="Test10"),
        sg.Button("Test11", size=(8, 1), key="Test11"),
        sg.Button("Test12", size=(8, 1), key="Test12"),
    ]
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


# nama image file temporary setiap kali processing output
filename_out = "out.png"

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
# Langkah 2 : Menampilkan list file citra pada folder yang dipilih
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

    elif event == "ImgList":  # A file was chosen from the listbox

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
            # img_input.show()

            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : "+str(img_width)+" x "+str(img_height))

            # Color depth
            mode_to_coldepth = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32,
                                "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : "+str(coldepth))
        except:
            pass
    elif event == "ImgSelect":

        try:
            filename2 = values["ImgSelect"]
            # print(filename2)
            img_input2 = Image.open(filename2)
            print(img_input2)
        except:
            pass

    elif event == "ImgNegative":

        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRotate90":

        try:
            window["ImgProcessingType"].update("Image Rotate 90")
            img_output = ImgRotate90(img_input, coldepth, 90)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRotate180":

        try:
            window["ImgProcessingType"].update("Image Rotate 180")
            img_output = ImgRotate180(img_input, coldepth, 180)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgRotate270":

        try:
            window["ImgProcessingType"].update("Image Rotate 270")
            img_output = ImgRotate270(img_input, coldepth, 270)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBrightness":

        try:
            value = int(values["input1"])
            window["ImgProcessingType"].update("Image Brightness")
            img_output = ImgBrightness(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgLogaritmic":

        try:
            value = int(values["input1"])
            window["ImgProcessingType"].update("Image Logaritmic")
            img_output = ImgLogaritmic(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgPowerLaw":

        try:
            value = int(values["input1"])
            window["ImgProcessingType"].update("Image Power Law")
            img_output = ImgPowerLaw(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgThreshold":

        try:
            value = int(values["input1"])
            print("ImgThreshold")
            window["ImgProcessingType"].update("Image Threshold")
            img_output = ImgThreshold(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBlending":

        try:
            c = float(values["input2"])
            window["ImgBlending"].update("Image Blending")
            img_output = ImgBlending(img_input, img_input2, coldepth, c)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslasiXY":

        try:
            print("ImgTranslasiXY")
            value = int(values["inputX"])
            value2 = int(values["inputY"])
            window["ImgTranslasiXY"].update("xy")
            img_output = ImgTranslasiXY(img_input, coldepth, value, value2)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslasiX":

        try:
            print("ImgTranslasiX")
            value = int(values["inputX"])
            window["ImgTranslasiX"].update("x")
            img_output = ImgTranslasiX(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgTranslasiY":

        try:
            print("ImgTranslasiY")
            value = int(values["inputY"])
            window["ImgTranslasiY"].update("y")
            img_output = ImgTranslasiY(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingHor":

        try:
            window["ImgFlippingHor"].update("Horizontal")
            img_output = ImgFlippingHor(img_input, coldepth, "horizontal")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingVer":

        try:
            window["ImgFlippingVer"].update("Vertical")
            img_output = ImgFlippingVer(img_input, coldepth, "vertical")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgFlippingHorVer":

        horver = "horizontalvertical"

        try:
            window["ImgFlippingHorVer"].update("Horizontal Vertical")
            img_output = ImgFlippingHorVer(img_input, coldepth, horver)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgZoomIn":

        try:
            value = int(values["skala"])
            window["ImgZoomIn"].update("Zoom In")
            img_output = ImgZoomIn(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgShrinking":

        try:
            value = int(values["skala"])
            window["ImgShrinking"].update("Zoom Out")
            img_output = ImgShrinking(img_input, coldepth, value)
            img_output.save(filename_out)
            img_output.save('shrink.png')
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test":

        try:
            window["Test"].update("Test")
            img_output = ImgTest(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test2":

        try:
            window["Test2"].update("Test2")
            img_output = ImgTest2(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test3":

        try:
            window["Test3"].update("Test3")
            img_output = ImgTest3(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test4":

        try:
            window["Test4"].update("Test4")
            img_output = ImgTest4(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test5":

        try:
            window["Test5"].update("Test5")
            img_output = ImgTest5(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test6":

        try:
            window["Test6"].update("Test6")
            img_output = ImgTest6(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test7":

        try:
            print('test7')
            window["Test7"].update("Test7")
            img_output = ImgTest7(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test8":

        try:
            print('test8')
            window["Test8"].update("Test8")
            img_output = ImgTest8(img_input, img_input2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test9":

        try:
            print('test9')
            window["Test9"].update("Test9")
            img_output = ImgTest9(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test10":

        try:
            print('test10')
            window["Test10"].update("Test10")
            img_output = ImgTest10(img_input, img_input2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test11":

        try:
            print('test11')
            window["Test11"].update("Test11")
            img_output = ImgTest11(img_input, img_input2, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "Test12":

        try:
            print('test12')
            window["Test12"].update("Test12")
            img_output = ImgTest12(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

window.close()
