from elegir_de_lista import elegir_indice, elegir_indice_azar, elegir_valor_azar, elegir_valor
from config import listas

repe = True

def main():
    lista_random = elegir_valor_azar(listas)
    makina = elegir_indice_azar(lista_random)
    opcion = elegir_indice(lista_random)
    valor_elemento = elegir_valor(lista_random, opcion)
    valor_elemento_random = elegir_valor(lista_random, makina)

    print(f"\n----------------------\nLa Maquina ha elegido la opcion {makina}\nElección: {valor_elemento_random}\n")
    print(f"\nTú has seleccionado la opcion {opcion}\nElección: {valor_elemento}\n")

while repe:
    main()
    repe = False
    decision = input(f"Quieres seguir jugando?")
    if "y" in decision:
        repe = True
    else:
        repe = False
    print(f"\n-------------------------------\n♥         Fin de juego        ♥\n-------------------------------\n")


