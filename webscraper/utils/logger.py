import logging
from config import LOG_FILE

def setup_logger():
    """Configura el logger para registrar eventos y errores en un archivo."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Logger configurado correctamente.")
