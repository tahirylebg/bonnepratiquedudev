from loguru import logger
import sys

"""" 
logger.remove() : Supprime les handlers par défaut

logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO") : Affiche les logs dans la 
console (avec couleur)

logger.add("logs/app.log", rotation="500 KB", level="INFO") : Sauvegarde les logs applicatifs

logger.add("logs/error.log", rotation="500 KB", level="ERROR") :# Sauvegarde les erreurs séparément

"""


logger.remove()

logger.add(sys.stdout, format="{time} | {level} | {message}", level="INFO")


logger.add("logs/app.log", rotation="500 KB", level="INFO")


logger.add("logs/error.log", rotation="500 KB", level="ERROR")

def get_logger():
    return logger

