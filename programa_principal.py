#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import obtencion_texto_imagenes

import obtencion_titulares_periodicos

import limpiar_pantalla

import time

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def informacion():
    print("\nMediante este código se puede mostrar el contenido de las etiquetas o descargar imágenes de los sitios web mediante Scraping usando las URL de los sitios\n")
    print("Permite la descarga de imágenes en formato PNG y JPG, se guardan en un directorio que se crea por defecto en la raíz al abrir con Visual Studio Code\n")
    time.sleep(2.5)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    print("\n1.- Obtención de texto o imágenes de sitios web a elección\n")
    print("\n2.- Obtención de titulares de periódicos\n")
    print("\n3.- Salir\n")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    #Inicialización de variable para que entre al bucle
    opcn_usuario = 1
    contador_limpieza = 0

    while opcn_usuario != 3:
        #Llamo a una función para que haga limpieza de la pantalla al inicio del bucle
        if contador_limpieza >= 1:
            limpiar_pantalla.limpieza_pantalla()
        
        contador_limpieza = contador_limpieza + 1

        #Muestro una pequeña información sobre el programa
        informacion()
        
        #Muestro las opciones disponibles
        menu()
        
        opcn_usuario = int(input("\nIntroduzca la opción que desea usar\n"))
        
        if opcn_usuario == 1:
            obtencion_texto_imagenes.funcion_scraping()
        elif opcn_usuario == 2:
            obtencion_titulares_periodicos.funcion_scraping()
        elif opcn_usuario == 3:
            print("\nPrograma finalizado")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ejecución del programa principal
if __name__ == "__main__":
    main()