import os

#---------------------------------------------------------------------------------
#Realiza limpieza de pantalla para sistemas basados en UNIX y en DOS
def limpieza_pantalla():
    #Realizo una pausa para que no se pierdan los resultados que se han mostrado
    input("\nPresione la tecla Enter o Intro para continuar...")
    
    comando = "clear"
    if os.name in ('nt', 'dos'):
        comando = "cls"
    os.system(comando)