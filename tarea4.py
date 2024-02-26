import shutil
import logging

# Configuración básica del registro
logging.basicConfig(filename='/home/ivan/logs/espacio.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Función para verificar el espacio en disco y registrar mensajes según el nivel de ocupación
def check_disk_space(partition):
    total, used, free = shutil.disk_usage(partition)
    percentage_used = (used / total) * 100

    if percentage_used > 80:
        logging.error("Espacio ocupado en la partición raíz es mayor que 80%.")
    elif percentage_used > 60:
        logging.warning("Espacio ocupado en la partición raíz es mayor que 60% pero menor que 80%.")
    else:
        logging.info("Espacio ocupado en la partición raíz es menor que 60%.")

def main():
    partition = "/"  # Partición raíz
    check_disk_space(partition)

if __name__ == "__main__":
    main()
