import re
import csv

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def procesar_usuarios(archivo_entrada, archivo_salida):
    usuarios = []
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
    except:
        print(f"Error al leer el archivo '{archivo_entrada}'")
        return

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue
        match = re.match(r'^(.*?)\s*-\s*(.*?)\s*-\s*(\d+)\s*años$', linea)
        if match:
            nombre, email, edad = match.groups()
            if validar_email(email.strip()):
                usuarios.append({'Nombre': nombre.strip(), 'Email': email.strip(), 'Edad': int(edad.strip())})
            else:
                print(f"Email inválido: {email.strip()}")
        else:
            print(f"Línea mal formateada: {linea}")

    try:
        with open(archivo_salida, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Nombre', 'Email', 'Edad'])
            writer.writeheader()
            for usuario in usuarios:
                writer.writerow(usuario)
        print(f"Archivo '{archivo_salida}' generado con {len(usuarios)} usuarios válidos.")
    except:
        print(f"Error al escribir el archivo '{archivo_salida}'")

if __name__ == "__main__":
    procesar_usuarios('usuarios.txt', 'usuarios_limpios.csv')
