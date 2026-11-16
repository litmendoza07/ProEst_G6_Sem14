import time
import random

#Generar intervalos
def generar_intervalos(cantidad):
    elementos = [
        max(1, cantidad // 4),
        max(1, cantidad //2),
        cantidad
    ]
    return sorted(set(elementos))


#Generar numeros
def generar_numeros(cantidad):
    inicio = time.perf_counter()
    datos = [random.randint(0, 5_000_000) for _ in range(cantidad)]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return datos, tiempo


# Ordenar los números aleatorios con el método de burbuja.
def ordenar_burbuja(datos):
    cantidad = len(datos)
    for i in range(cantidad):
        hubo_intercambio = False
        for j in range(cantidad - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break
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
datos = ordenar_burbuja(datos)
fin_ordenamiento = time.perf_counter()
print(f"Tiempo de ordenamiento: {fin_ordenamiento - inicio_ordenamiento:.4f} segundos")
print("Números ordenados:")
print(datos)

