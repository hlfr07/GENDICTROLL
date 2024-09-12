import random
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

def generar_contraseña(longitud_min, longitud_max, caracteres_seleccionados):
    # Genera contraseñas desde longitud mínima hasta longitud máxima
    contraseñas = []
    for longitud in range(longitud_min, longitud_max + 1):
        combinaciones = generar_combinaciones(longitud, caracteres_seleccionados)
        contraseñas.extend(combinaciones)  # Agregar todas las combinaciones de esa longitud
    return contraseñas

def generar_combinaciones(longitud, caracteres_seleccionados):
    # Genera todas las combinaciones posibles de los caracteres seleccionados con la longitud especificada
    combinaciones = [''.join(c) for c in itertools.product(caracteres_seleccionados, repeat=longitud)]
    return combinaciones

def generar_contraseñas_con_patron(patron, caracteres_seleccionados):
    # Genera todas las combinaciones posibles para los asteriscos (*) en el patrón
    num_asteriscos = patron.count('*')
    
    if num_asteriscos == 0:
        return [patron]  # Si no hay asteriscos, se devuelve el patrón tal cual
    
    # Genera todas las combinaciones posibles para los asteriscos
    combinaciones = generar_combinaciones(num_asteriscos, caracteres_seleccionados)
    
    contraseñas_generadas = []
    
    for combinacion in combinaciones:
        temp_patron = patron
        for char in combinacion:
            temp_patron = temp_patron.replace('*', char, 1)  # Reemplaza un * a la vez
        contraseñas_generadas.append(temp_patron)
    
    return contraseñas_generadas

def guardar_contraseña_en_archivo(nombre_archivo, contraseñas):
    with open(f"{nombre_archivo}.txt", "w") as archivo:
        for contraseña in contraseñas:
            archivo.write(contraseña + '\n')
    print(f"Contraseñas guardadas en el archivo {nombre_archivo}.txt")

def seleccionar_caracteres_predefinidos():
    # Permite seleccionar los tipos de caracteres que se utilizarán para la generación de contraseñas
    print("Selecciona los caracteres a usar:")
    print("1. Números")
    print("2. Minúsculas")
    print("3. Mayúsculas")
    print("4. Caracteres especiales")
    seleccion = input("Introduce el número o combinación de números según los caracteres deseados (Ej: 123): ")

    caracteres_seleccionados = ""
    if '1' in seleccion:
        caracteres_seleccionados += string.digits
    if '2' in seleccion:
        caracteres_seleccionados += string.ascii_lowercase
    if '3' in seleccion:
        caracteres_seleccionados += string.ascii_uppercase
    if '4' in seleccion:
        caracteres_seleccionados += string.punctuation
    
    if caracteres_seleccionados == "":
        print("No has seleccionado ningún tipo de caracteres. Inténtalo de nuevo.")
        return seleccionar_caracteres_predefinidos()  # Reintentar si no se seleccionó nada
    else:
        return caracteres_seleccionados

def seleccionar_caracteres_personalizados():
    # Permite ingresar manualmente los caracteres que se usarán
    caracteres_personalizados = input("Introduce los caracteres que deseas usar para generar las contraseñas (Ej: ABCaw123¨?*): ")
    
    if not caracteres_personalizados:
        print("No has ingresado ningún carácter. Inténtalo de nuevo.")
        return seleccionar_caracteres_personalizados()  # Reintentar si no se ingresó nada
    else:
        return caracteres_personalizados

def seleccionar_caracteres():
    # Preguntar si se quieren usar caracteres predefinidos o personalizados
    usar_predefinidos = input("¿Quieres usar caracteres predefinidos de la lista? (si/no): ").lower()
    
    if usar_predefinidos == "si":
        return seleccionar_caracteres_predefinidos()
    else:
        return seleccionar_caracteres_personalizados()

def main():
    mostrar_bienvenida()  # Mostrar la bienvenida al iniciar el programa

    generar = input("¿Quieres generar una contraseña? (si/no): ").lower()
    
    if generar == "si":
        caracteres_seleccionados = seleccionar_caracteres()  # Permite seleccionar los caracteres a usar
        
        usar_patrones = input("¿Usarás patrones predefinidos? (si/no): ").lower()
        
        if usar_patrones == "si":
            # Generación con patrón personalizado
            patron_personalizado = input("Introduce el patrón personalizado (usa * para los caracteres a generar): ")
            contraseñas = generar_contraseñas_con_patron(patron_personalizado, caracteres_seleccionados)
        
        else:
            # Si no se usan patrones, pedir la longitud mínima y máxima
            longitud_min = int(input("Introduce la longitud mínima: "))
            longitud_max = int(input("Introduce la longitud máxima: "))
            
            # Genera todas las combinaciones posibles para cada longitud desde min hasta max
            contraseñas = generar_contraseña(longitud_min, longitud_max, caracteres_seleccionados)
        
        nombre_archivo = input("¿Qué nombre tendrá el archivo donde se guardará la contraseña?: ")
        guardar_contraseña_en_archivo(nombre_archivo, contraseñas)
    
    else:
        print("No se generó ninguna contraseña.")

if __name__ == "__main__":
    main()
