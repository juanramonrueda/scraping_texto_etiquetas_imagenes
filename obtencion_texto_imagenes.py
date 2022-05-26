#---------------------------------------------------------------------------------------------------------------
import requests

from bs4 import BeautifulSoup

import wget

import os

#---------------------------------------------------------------------------------------------------------------
def funcion_scraping():
    obtener_datos()

#---------------------------------------------------------------------------------------------------------------
#Pido al usuario la URL y la etiqueta deseada
def obtener_datos():
    #-----------------------------------------------------------------------------------------------------------
    #Obtención de la URL y almacenamiento mediante REQUESTS.GET en PAGINA
    url_usuario = str(input("\nIntroduzca la URL, sin 'http://' o 'https://'\n"))
    url = "http://" + str(url_usuario)

    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")

    #-----------------------------------------------------------------------------------------------------------
    #Obtención del tipo de etiqueta de la que quiere sacar información
    tipo_etiqueta = str(input("\nIntroduzca la etiqueta de la que quiere obtener información\n"))

    etiqueta = soup.find_all(tipo_etiqueta)

    #-----------------------------------------------------------------------------------------------------------
    #Dependiendo del tipo de etiqueta que introduzca el usuario realizará una acción u otra
    if tipo_etiqueta != "img":
        obtencion_resultados_texto(etiqueta)
    else:
        descarga_imagenes(etiqueta)

#---------------------------------------------------------------------------------------------------------------
#Realización de la obtención mediante la Biblioteca BeautifulSoup y la etiqueta introducida
def obtencion_resultados_texto(etiqueta):
    print() #Para dejar una separación entre los datos anteriores y los mostrados
    for resultado in etiqueta:
        print(resultado.text.strip())

#---------------------------------------------------------------------------------------------------------------
#Creo un directorio al que se van todas las imágenes, por defecto es el que tiene Visual Studio Code como raíz
def crear_directorio_descarga():
    crear_directorio = ("directorio_imagenes")

    os.mkdir(crear_directorio)

    return crear_directorio

#----------------------------------------------------------------------------------------------------------------
def descarga_imagenes(etiqueta):

    directorio_descarga = crear_directorio_descarga()

    for imagen in etiqueta:
        try:
            print(imagen['src'])
            url_imagen = imagen['src']
            if url_imagen.endswith('.jpg') or url_imagen.endswith('.png'):
                wget.download(url_imagen, out=directorio_descarga)

        except KeyError:
            pass