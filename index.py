import click
import requests
from termcolor import colored
from PIL import Image
import os

@click.group()
def main():
    pass



@main.command() 
@click.option("--path", "-p", default="/home/dayrons/Descargas/")
@click.option("--output", "-o", default="~/")
def compress_img(path, output):

    try:
        os.mkdir(path+"compressed")
    except :
        pass

    for file in os.listdir(path):

        name, extens =  os.path.splitext(path+file)
        if extens in [".jpg",".jpeg", ".png"]:
            picture = Image.open(path + file)
            picture.save(path + "compressed/compressed_"+file, optimize=True, quality=60)
            os.remove(path+file)
    print(colored("Compresion finalizada", "green"))
            

if __name__ == "__main__":
    main()