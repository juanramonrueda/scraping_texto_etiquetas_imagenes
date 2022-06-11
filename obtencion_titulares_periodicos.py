#--------------------------------------------------------------------------
import requests

from bs4 import BeautifulSoup

#--------------------------------------------------------------------------
#Defino la función que mostrará los titulares de los periódicos
def funcion_scraping():
    contador = 0

    mostrar_periodicos()

    url = elegir_periodico()

    paginas = requests.get(url)

    soup = BeautifulSoup(paginas.content, "html.parser")

    periodicos = soup.find_all("h2")

    for periodico in periodicos:
        print(f"{periodico.text.strip()}\n")

        #------------------------------------------------------------------
        #Preparo un contador para que muestre los diez primeros resultados
        contador = contador + 1
        if contador == 10:
            break

#--------------------------------------------------------------------------
#Muestro las opciones disponibles
def mostrar_periodicos():
    print("\nLos periódicos a elegir son:\n")
    print("1.- Eldiario\n")
    print("2.- El País\n")
    print("3.- Marca\n")
    print("4.- Mundo Deportivo\n")
    print("5.-El Economista\n")

#--------------------------------------------------------------------------
def elegir_periodico():
    #Realizo la elección del usuario del periódico que quiere consultar
    eleccion = int(input("Elija el periodico\n"))
    
    if eleccion == 1:
        url = "https://www.eldiario.es/"
    elif eleccion == 2:    
        url = "https://elpais.com/"
    elif eleccion == 3:
        url = "https://www.marca.com/"
    elif eleccion == 4:
        url = "https://www.mundodeportivo.com/"
    elif eleccion == 5:
        url = "https://www.eleconomista.es/"

    return url
