def mover_ceros_al_final(lista):
    # Inicializamos un identificador de posición para llevar la cuenta de la posición
    posicion = 0

    for i in range(len(lista)):
        # Si el elemento actual no es cero, lo movemos hacia la izquierda
        if lista[i]!= 0:
            lista[posicion] = lista[i]
            posicion += 1

    # Llenamos el resto de la lista con ceros
    while posicion < len(lista):
        lista[posicion] = 0
        posicion += 1

    return lista

print("Ingrese los números reales separados por espacios. Para terminar, ingrese 'fin'.")
numeros = []
while True:
    entrada = input("Ingrese un número: ")
    if entrada == "fin":
        break
    numeros.append(float(entrada))

resultado = mover_ceros_al_final(numeros)
print("Lista con ceros al final:", resultado)