import string
import itertools

def mostrar_bienvenida():
    # Mostrar la bienvenida en formato ASCII
    print("                                     ▒▒▒▒■■■■■■■■■■■■■■")
    print("                                     ▒▒▒▒")
    # Tu arte ASCII permanece igual

def guardar_contraseña_en_archivo_generador(nombre_archivo, generador):
    with open(f"{nombre_archivo}.txt", "w") as archivo:
        contador = 0
        for contraseña in generador:
            archivo.write(contraseña + '\n')  # Escribe cada contraseña en el archivo
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

def generar_contraseñas_con_patron_generador(patron, caracteres_seleccionados):
    # Generador para generar contraseñas usando un patrón
    num_asteriscos = patron.count('*')
    if num_asteriscos == 0:
        yield patron
    else:
        combinaciones = generar_combinaciones_generador(num_asteriscos, caracteres_seleccionados)
        for combinacion in combinaciones:
            temp_patron = patron
            for char in combinacion:
                temp_patron = temp_patron.replace('*', char, 1)
            yield temp_patron

def seleccionar_caracteres_predefinidos():
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

    if not caracteres_seleccionados:
        print("No has seleccionado ningún tipo de caracteres. Inténtalo de nuevo.")
        return seleccionar_caracteres_predefinidos()
    return caracteres_seleccionados

def seleccionar_caracteres_personalizados():
    caracteres_personalizados = input("Introduce los caracteres que deseas usar para generar las contraseñas (Ej: ABCaw123¨?*): ")
    if not caracteres_personalizados:
        print("No has ingresado ningún carácter. Inténtalo de nuevo.")
        return seleccionar_caracteres_personalizados()
    return caracteres_personalizados

def seleccionar_caracteres():
    usar_predefinidos = input("¿Quieres usar caracteres predefinidos de la lista? (si/no): ").lower()
    if usar_predefinidos == "si":
        return seleccionar_caracteres_predefinidos()
    return seleccionar_caracteres_personalizados()

def main():
    mostrar_bienvenida()

    generar = input("¿Quieres generar una contraseña? (si/no): ").lower()

    if generar == "si":
        caracteres_seleccionados = seleccionar_caracteres()

        usar_patrones = input("¿Usarás patrones predefinidos? (si/no): ").lower()

        if usar_patrones == "si":
            patron_personalizado = input("Introduce el patrón personalizado (usa * para los caracteres a generar): ")
            generador = generar_contraseñas_con_patron_generador(patron_personalizado, caracteres_seleccionados)
        else:
            longitud_min = int(input("Introduce la longitud mínima: "))
            longitud_max = int(input("Introduce la longitud máxima: "))
            generador = generar_contraseñas_generador(longitud_min, longitud_max, caracteres_seleccionados)

        nombre_archivo = input("¿Qué nombre tendrá el archivo donde se guardará la contraseña?: ")
        guardar_contraseña_en_archivo_generador(nombre_archivo, generador)
    else:
        print("No se generó ninguna contraseña.")

if __name__ == "__main__":
    main()
