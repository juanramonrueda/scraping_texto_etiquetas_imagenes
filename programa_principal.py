#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import obtencion_texto_imagenes

import time

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def informacion():
    print("\nMediante este código se puede mostrar el contenido de las etiquetas o descargar imágenes de los sitios web mediante Scraping usando las URL de los sitios\n")
    print("\nEste programa permite la descarga de imágenes en formato PNG y JPG, se guardan en un directorio que se crea por defecto en la raíz al abrir con Visual Studio Code\n")
    time.sleep(2.5)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    informacion()
    obtencion_texto_imagenes.funcion_scraping()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()