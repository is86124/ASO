import psutil

def obtener_porcentaje_espacio(particion):
    espacio = psutil.disk_usage(particion)
    porcentaje = espacio.percent
    return porcentaje

def main():
    particiones = ["/dev/sda1"]  # Lista de las particiones que quieres verificar
    for particion in particiones:
        porcentaje = obtener_porcentaje_espacio(particion)
        print(f"{particion} {porcentaje:.1f}%")

if __name__ == "__main__":
    main()