from elegir_de_lista import elegir_indice, elegir_indice_azar, elegir_valor_azar, elegir_valor
from config import listas

repe = True

def main():
    lista = elegir_valor_azar(listas)
    makina = elegir_indice_azar(listas)
    opcion = elegir_indice(lista)
    valor_elemento = elegir_valor(lista, opcion)
    valor_elemento_random = elegir_valor(lista, makina)

    print(f"\n-------------------------------\nLa Maquina ha elegido la opcion {makina}\nElección: {valor_elemento_random}\n")
    print(f"\nTú has seleccionado la opcion {opcion}\nElección: {valor_elemento}\n")

while repe:
    main()
    repe = False
    desicion =input(f"Quieres seguir jugando?")
    if desicion == "y":
        repe = True
    else:
        break





