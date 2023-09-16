import random


def generar_datos(num_filas, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("S_i,A_i\n")
        for i in range(num_filas):
            numero1 = random.randint(0, num_filas * 10)
            numero2 = random.randint(0, num_filas * 10)
            linea = f"{numero1}, {numero2}\n"
            archivo.write(linea)
        archivo.close()
