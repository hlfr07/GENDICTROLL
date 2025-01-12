import string
import itertools

def mostrar_bienvenida():
    # Mostrar la bienvenida en formato ASCII
    print("                                     ░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄")
    print("                                     ░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄")
    print("                                     ░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█") 
    print("                                     ░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█")
    print("                                     ░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█")
    print("                                     █▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█")
    print("                                     █▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█")
    print("                                     ░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█")
    print("                                     ░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█")
    print("                                     ░░░█░░██░░▀█▄▄▄█▄▄█▄████░█")
    print("                                     ░░░░█░░░▀▀▄░█░░░█░███████░█")
    print("                                     ░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█")
    print("                                     ░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█")
    print("                                     ░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█")
    print("                                     ░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█")
    print("")
    print("                                               ¯\\_(ツ)_/¯")
    print("                              __________________________________________________")					
    print("                                ︻デ═一  Created by: XDeadHackerX v2.2  ︻デ═一 ") 
    print("          -------------------------------------------------------------------------------------------")
    print("          Cualquier acción y o actividad relacionada con Wifi_Troll es únicamente su responsabilidad")
    print("          -------------------------------------------------------------------------------------------")

def guardar_contraseña_en_archivo_generador(nombre_archivo, generador):
    with open(f"{nombre_archivo}.txt", "w") as archivo:
        contador = 0
        for contraseña in generador:
            archivo.write(contraseña + '\n')
            contador += 1
    print(f"Contraseñas guardadas en el archivo {nombre_archivo}.txt")
    print(f"Se generaron {contador} contraseñas en total.")

def generar_combinaciones_generador(longitud, caracteres_seleccionados):
    # Generador que produce combinaciones una por una
    return (''.join(c) for c in itertools.product(caracteres_seleccionados, repeat=longitud))

def generar_contraseñas_generador(longitud_min, longitud_max, caracteres_seleccionados):
    # Generador que produce combinaciones desde longitud mínima hasta máxima
    for longitud in range(longitud_min, longitud_max + 1):
        yield from generar_combinaciones_generador(longitud, caracteres_seleccionados)

def main():
    mostrar_bienvenida()

    generar = input("¿Quieres generar una contraseña? (si/no): ").lower()
    if generar == "si":
        caracteres_seleccionados = string.ascii_lowercase + string.digits  # Ejemplo de selección de caracteres
        
        longitud_min = int(input("Introduce la longitud mínima: "))
        longitud_max = int(input("Introduce la longitud máxima: "))
        
        nombre_archivo = input("¿Qué nombre tendrá el archivo donde se guardará la contraseña?: ")
        
        generador = generar_contraseñas_generador(longitud_min, longitud_max, caracteres_seleccionados)
        guardar_contraseña_en_archivo_generador(nombre_archivo, generador)
    else:
        print("No se generó ninguna contraseña.")

if __name__ == "__main__":
    main()
