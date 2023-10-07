import random

def generar_datos(dias, nombre_archivo, variacion_e, variacion_s):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"{dias}\n")
        
        energia = []
        descanso = []
        for i in range(dias):
            energia.append(random.randint(0, dias * variacion_e))
            descanso.append(random.randint(0, dias * variacion_s))
          
        descanso = sorted(descanso, reverse=True)
        
        for e in energia:
          archivo.write(f"{e}\n")
        
        for d in descanso:
          archivo.write(f"{d}\n")
          
        archivo.close()
