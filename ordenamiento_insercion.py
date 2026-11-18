import time
import random


def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


def ordenar_insercion(datos):
    for i in range(1, len(datos)):
        actual = datos[i]
        j = i - 1

        while j >= 0 and datos[j] > actual:
            datos[j + 1] = datos[j]
            j -= 1

        datos[j + 1] = actual

    return datos


cantidad = int(input("Cantidad de elementos: "))
datos, tiempo_generacion = generar_numeros(cantidad)
print("Iniciar generación.")
print(f"Tiempo de generación: {tiempo_generacion:.4f} segundos")
print("Fin de generación.")
print("Números generados:", datos)

inicio_ordenamiento = time.perf_counter()
ordenar_insercion(datos)
tiempo_ordenamiento = time.perf_counter() - inicio_ordenamiento
print(f"\nEl tiempo que tardó en ordenar los números aleatorios fue: {tiempo_ordenamiento:.6f} segundos")
print("Números ordenados:", datos)