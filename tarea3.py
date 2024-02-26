import os

def crear_carpetas_y_ficheros():
    for i in range(1, 6):  # Itera 5 veces
        nombre_carpeta = f"folder{i}"
        os.makedirs(nombre_carpeta, exist_ok=True)  # Crea la carpeta si no existe
        for j in range(1, 11):  # Crea 10 archivos dentro de cada carpeta
            nombre_fichero = f"{nombre_carpeta}/fichero{j}.txt"
            with open(nombre_fichero, 'w') as archivo:
                archivo.write(f"Este es el contenido del fichero {j}\n")
        print(f"Se crearon los archivos en la carpeta {nombre_carpeta}")

def main():
    crear_carpetas_y_ficheros()

if __name__ == "__main__":
    main()
