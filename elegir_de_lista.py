import random
from pideUnNum import pideUnNum 

def presentacion(lista):
    contador = 0
    msg = "ELIGE UNA OPCION: \n"
    for opcion in lista:
        msg += f" - {contador} - {opcion}\n"
        contador +=1
    print(msg)

def elegir_indice(lista):
    presentacion(lista)
    opcion = pideUnNum()
    while opcion not in range(len(lista)):
        print("Introduce un numero dentro del rango")
        opcion = pideUnNum()

    return opcion

def elegir_valor(lista,opcion):
    return lista[opcion]

def elegir_indice_azar(listas):
    return random.randrange(len(listas))

def elegir_valor_azar(lista):
    return random.choice(lista)

