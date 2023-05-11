from elegir_de_lista import elegir_indice, elegir_indice_azar, elegir_valor_azar, elegir_valor
from config import listas


def main():
    lista = elegir_valor_azar(listas)
    makina = elegir_indice_azar(listas)
    opcion = elegir_indice(lista)
    valor_elemento = elegir_valor(lista, opcion)
    valor_elemento_random = elegir_valor(lista, makina)

    print(f"\nLa Maquina ha elegido la opcion {makina}, la cual es {valor_elemento_random}\n")
    print(f"\nTú has seleccionado la opcion {opcion} ")
    print(f"\nElección: {valor_elemento}")
    print()

main()
