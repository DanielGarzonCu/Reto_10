def calcular_promedio(numeros):

    total = 0.0
    for numero in numeros:
        total += numero
    # Calcula el promedio dividiendo la suma total por el número de elementos
    return total / len(numeros)

if __name__ == "__main__":
    entrada = input("Ingresa una lista de números reales separados por espacios: ")
    numeros = []
    # Inicializa una variable para construir cada número a partir del string de entrada principalmente porque sin esto no permitiria la entrada de un valor real
    valor = ""
  
    for char in entrada:
        # Si el carácter no es un espacio, agrégalo al número actual
        if char!= " ":
            valor += char
        # Si el carácter es un espacio, agrega el número actual a la lista y reinicia el valor
        else:
            numeros.append(float(valor))
            valor = ""
    # Agrega el último número a la lista si no está vacío
    if valor!= "":
        numeros.append(float(valor))

    promedio = calcular_promedio(numeros)
    print(f"El promedio de los números es: {promedio}")