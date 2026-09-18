import json
import os

RUTA_ARCHIVO = os.path.join("data", "citas.json")

def cargar_citas() -> list:
    """Lee el archivo JSON de citas con manejo de excepciones."""
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_citas(citas: list) -> bool:
    """Escribe la lista de citas en formato JSON con indentación y soporte UTF-8."""
    try:
        # Asegura la existencia de la carpeta data
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(citas, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"\n[Error] No se pudieron guardar los datos: {e}")
        return False