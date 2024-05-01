# Reto_10
# ¡PYTHON FC!

<details>
  <summary>¡ESCUDO!</summary>
  
  [![PYTHON-F-C-B.jpg](https://i.postimg.cc/1Xpw71f0/PYTHON-F-C-B.jpg)](https://postimg.cc/jnSDC96C)

</details>

# 1 
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```ruby
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
```
# 2
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```ruby
if __name__ == "__main__":
    
    # Crear listas vacías para almacenar los componentes de los vectores
    vector_primero = []
    vector_segundo = []
    resultado = []
    flotante = ""

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
    flotante = ""
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

    # Determinar la longitud del vector más corto pues es la que se tiene en cuenta a la hora de encontrar el producto punto
    longitud = len(vector_primero) if len(vector_primero) < len(vector_segundo) else len(vector_segundo)
    for i in range(longitud):
        # Calcular el producto punto de los vectores
        if i < len(vector_primero) and i < len(vector_segundo):
            resultado.append(vector_primero[i] * vector_segundo[i])

    producto_punto = resultado 
    print(f"El producto punto de los vectores es: {resultado}")
```
# 3 
Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```ruby
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

print("Ingrese los números separados por espacios. Para terminar, ingrese 'fin'.")
numeros = []
while True:
    entrada = input("Ingrese un número: ")
    if entrada == "fin":
        break
    numeros.append(float(entrada))

resultado = mover_ceros_al_final(numeros)
print("Lista con ceros al final:", resultado)
```
