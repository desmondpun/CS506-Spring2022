from PIL import Image, ImageDraw
import PySimpleGUI as PySimpleGUI
from PIL import Image
import os
import tkinter
import io

def draw_policestation():
    img = Image.open("policestation.jpeg")
    img.thumbnail((1200, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    layout = [[[sg.Text("Firestation:", font = ("Arial", 25)),],[sg.Image(data=bio.getvalue())]], [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Image", layout, size=(1200, 800))

    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break

    window.close()

draw_policestation()