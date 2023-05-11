from elegir_de_lista import elegir_indice, elegir_valor_azar, elegir_indice_azar, elegir_valor
from config import listas


def main():
    lista = elegir_valor_azar(listas)
    makina = elegir_indice_azar(listas)
    opcion = elegir_indice(lista)

    print(f"\nLa Maquina ha elegido la opcion {makina}, la cual es {lista[makina]}\n")
    print(f"\nTú has seleccionado la opcion {opcion} ")
    print(f"\nElección: {lista[opcion]}")
    print()

main()
