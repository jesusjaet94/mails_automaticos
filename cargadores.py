from pathlib import Path

CARPETA_BASE = Path(__file__).resolve().parent


def cargar_credenciales(nombre_archivo="credenciales.txt"):
    ruta = CARPETA_BASE / nombre_archivo
    credenciales = {}
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea and "=" in linea:
                    clave, valor = linea.split("=", 1)
                    credenciales[clave.strip()] = valor.strip()
        return credenciales
    except FileNotFoundError:
        print(f"[Error] No se encontró '{nombre_archivo}'")
        return {}


def cargar_destinatarios(nombre_archivo="destinatarios.txt"):
    ruta = CARPETA_BASE / nombre_archivo
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"[Error] No se encontró '{nombre_archivo}'")
        return []


def cargar_enviados(nombre_archivo="enviados.txt"):
    ruta = CARPETA_BASE / nombre_archivo
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return {linea.strip() for linea in archivo if linea.strip()}
    except FileNotFoundError:
        return set()


def cargar_presentacion(nombre_archivo="presentacion.txt"):
    ruta = CARPETA_BASE / nombre_archivo
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read().strip()
    except FileNotFoundError:
        print(f"[Error] No se encontró '{nombre_archivo}'")
        return ""


def cargar_cv(nombre_archivo="cv.pdf"):
    ruta = CARPETA_BASE / nombre_archivo
    try:
        with open(ruta, "rb") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"[Error] No se encontró '{nombre_archivo}'")
        return None


def registrar_enviado(correo, nombre_archivo="enviados.txt"):
    ruta = CARPETA_BASE / nombre_archivo
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{correo}\n")