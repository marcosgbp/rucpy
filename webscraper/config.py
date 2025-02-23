# config.py
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Variables generales
DOWNLOAD_URL = os.getenv("DOWNLOAD_URL")
TEMP_DIR = os.getenv("TEMP_DIR")
EXTRACT_DIR = os.getenv("EXTRACT_DIR")
LOG_FILE = os.getenv("LOG_FILE")

# Configuración de la base de datos
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# Configuración de los archivos
ENCODING = os.getenv("ENCODING")
DELIMITER = os.getenv("DELIMITER")
