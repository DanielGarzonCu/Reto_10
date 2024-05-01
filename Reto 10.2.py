if __name__ == "__main__":
    
    # Crear listas vacías para almacenar los componentes de los vectores
    vector_primero = []
    vector_segundo = []
    resultado = []
    flotante = []

    # Pedir al usuario que ingrese los componentes del primer vector
    entrada1 = input("Ingrese la cantidad de componentes del primer vector separados por espacios: ")
    for x in entrada1:
        # Agregar cada caracter a la variable flotante hasta que se encuentre un espacio
        if x!= " ":
            flotante += x
        else:
            # Convertir la variable flotante a un número flotante y agregarlo al vector_primero
            vector_primero.append(float(flotante))
            flotante = ""
    # Agregar el último número flotante al vector_primero si no es vacío
    if flotante!= "":
        vector_primero.append(float(flotante))

    # Resetear la variable flotante para el segundo vector
    flotante = []
    # Pedir al usuario que ingrese los componentes del segundo vector
    entrada2 = input("Ingrese la cantidad de componentes del segundo vector separados por espacios: ")
    for x in entrada2:
        # Agregar cada caracter a la variable flotante hasta que se encuentre un espacio
        if x!= " ":
            flotante += x
        else:
            # Convertir la variable flotante a un número flotante y agregarlo al vector_segundo
            vector_segundo.append(float(flotante))
            flotante = ""
    # Agregar el último número flotante al vector_segundo si no es vacío
    if flotante!= "":
        vector_segundo.append(float(flotante))

    # Determinar la longitud del vector más corto
    longitud = len(vector_primero) if len(vector_primero) < len(vector_segundo) else len(vector_segundo)
    for i in range(longitud):
        # Calcular el producto punto de los vectores
        if i < len(vector_primero) and i < len(vector_segundo):
            resultado.append(vector_primero[i] * vector_segundo[i])
        elif i < len(vector_primero):
            resultado.append(vector_primero[i] * 1)
        else:
            resultado.append(vector_segundo[i] * 1)

    # Asignar el resultado del producto punto a la variable producto_punto
    producto_punto = resultado 
    # Imprimir el resultado del producto punto
    print(f"El producto punto de los vectores es: {resultado}")