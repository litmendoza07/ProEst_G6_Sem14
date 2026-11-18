import time
import random


# Generar numeros
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


# Ordenar los números aleatorios con el método de selección.
def ordenar_seleccion(datos):
    cantidad = len(datos)
    for i in range(cantidad - 1):
        indice_menor = i
        for j in range(i + 1, cantidad):
            if datos[j] < datos[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            datos[i], datos[indice_menor] = datos[indice_menor], datos[i]
    return datos


cantidad = int(input("Cantidad de elementos: "))
datos, tiempo = generar_numeros(cantidad)
print("Iniciar generación.")
print(f"Tiempo de generación: {tiempo:.4f} segundos")
print("Fin de generación.")
ini = time.perf_counter()
print(datos)
fin = time.perf_counter()
dif = fin - ini
print(f"Duración de impresión: {dif:.4f} segundos")

inicio_ordenamiento = time.perf_counter()
datos = ordenar_seleccion(datos)
fin_ordenamiento = time.perf_counter()
print(f"Tiempo de ordenamiento: {fin_ordenamiento - inicio_ordenamiento:.4f} segundos")
print("Números ordenados:")
print(datos)
