import subprocess
import os
import sys

def run_spider():
    """Ejecuta el spider de Scrapy."""
    # Cambia al directorio del spider
    spider_directory = "crawler"  # Ajusta esto según el nombre de tu carpeta
    os.chdir(spider_directory)

    print("Ejecutando el spider...")
    result = subprocess.run(['scrapy', 'crawl', 'crawler'], capture_output=True, text=True)

    # Volver al directorio anterior
    os.chdir("..")  # Regresar al directorio raíz

    # Verificamos si el spider se ejecutó correctamente
    if result.returncode != 0:
        print("Error al ejecutar el spider:")
        print(result.stderr)
        sys.exit(1)
    else:
        print("Spider ejecutado correctamente.")

def upload_to_git():
    """Sube el archivo generado al repositorio de Git."""
    file_path = "lista.m3u"  # Asegúrate de que este sea el nombre correcto

    # Verificamos si el archivo existe
    if not os.path.exists(file_path):
        print(f"Error: El archivo {file_path} no existe.")
        sys.exit(1)

    # Comprobamos si estamos en un repositorio de Git
    if not os.path.exists('.git'):
        print("Error: No se encuentra un repositorio de Git en el directorio actual.")
        sys.exit(1)

    # Comandos de git
    try:
        # Añadir archivo al área de preparación
        subprocess.run(['git', 'add', file_path], check=True)
        print(f"Añadiendo {file_path} al área de preparación...")

        # Hacer un commit
        commit_message = "Actualización del archivo de canales"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("Commit realizado.")

        # Subir al repositorio
        subprocess.run(['git', 'push'], check=True)
        print("Archivo subido al repositorio correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error en el proceso de git: {e}")

if __name__ == "__main__":
    run_spider()
    upload_to_git()
