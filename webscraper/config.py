# config.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# URL principal de la página que contiene los enlaces de descarga
PAGE_URL = os.getenv("PAGE_URL")
BASE_URL = os.getenv("BASE_URL")

# Rutas de almacenamiento temporal
TEMP_DIR = os.getenv("TEMP_DIR", "temp/")
EXTRACT_DIR = os.getenv("EXTRACT_DIR", "extracted/")
LOG_FILE = os.getenv("LOG_FILE", "logs/scraper.log")

# Configuración de la base de datos MySQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Configuración general de los archivos
ENCODING = os.getenv("ENCODING", "utf-8")
DELIMITER = os.getenv("DELIMITER", "|")
