from pideUnNum import pideUnNum 

def presentacion(lista):
    contador = 0
    msg = "ELIGE UNA OPCION: \n"
    for opcion in lista:
        msg += f" - {contador} - {opcion}\n"
        contador +=1
    print(msg)

def elegirlista(lista):
    opcion = pideUnNum()
    if opcion in range(len(lista)):
        print(f"Has elegido el elemento {lista[opcion]}")
    else:
        print("mete un numero del 0 al 4")
        elegirlista(lista)
    return opcion

# if __name__ == "__main__":
#     lista = ["piedra", "papelito", "manostijeras", "lacoste", "Spock"]
