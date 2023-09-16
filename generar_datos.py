import random


def generar_datos(num_filas, nombre_archivo, variacion_s, variacion_a):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("S_i,A_i\n")
        for i in range(num_filas):
            S_i = random.randint(0, num_filas * variacion_s)
            A_i = random.randint(0, num_filas * variacion_a)
            linea = f"{S_i}, {A_i}\n"
            archivo.write(linea)
        archivo.close()
