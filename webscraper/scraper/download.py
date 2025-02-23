import os
import re
import requests
import logging
from bs4 import BeautifulSoup
from datetime import datetime
from config import PAGE_URL, BASE_URL, TEMP_DIR

def get_download_links() -> list:
    """
    Extrae los enlaces de descarga de los archivos ZIP desde la página de la DNIT.
    Devuelve una lista con las URLs completas.
    """
    try:
        logging.info("Solicitando la página principal para extraer enlaces.")
        response = requests.get(PAGE_URL, timeout=60)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        #print(soup)
        # Buscar todos los enlaces dentro de la clase contenedora
        for link in soup.select('.list__item.search-item div.item__links a.link'):
            
            href = link.get('href')
           
            if href and "ruc" in href and ".zip" in href:
                full_url = BASE_URL + href
                print(full_url)
                links.append(full_url)

        logging.info(f"Se encontraron {len(links)} enlaces de descarga.")
        return links

    except requests.RequestException as e:
        logging.error(f"Error al solicitar la página principal: {e}")
        raise

def download_files(links: list) -> list:
    """
    Descarga los archivos ZIP de las URLs proporcionadas y los guarda en la carpeta TEMP_DIR.
    Devuelve una lista con las rutas locales de los archivos descargados.
    """
    file_paths = []

    # Crear la carpeta TEMP_DIR si no existe
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    for url in links:
        try:
            # Obtener el nombre correcto del archivo ZIP
            filename = re.search(r'ruc\d+\.zip', url).group(0)
            file_path = os.path.join(TEMP_DIR, filename)

            logging.info(f"Descargando archivo: {filename} desde {url}")

            # Descargar el archivo
            response = requests.get(url, stream=True, timeout=60)
            response.raise_for_status()

            # Guardar el archivo en TEMP_DIR
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            logging.info(f"Archivo guardado: {file_path}")
            file_paths.append(file_path)

        except (requests.RequestException, AttributeError) as e:
            logging.error(f"Error al descargar el archivo desde {url}: {e}")

    return file_paths