from cargadores import (
    cargar_credenciales,
    cargar_cv,
    cargar_destinatarios,
    cargar_enviados,
    cargar_presentacion,
    registrar_enviado,
)
from enviador import enviar_tanda

CLAVES_REQUERIDAS = {
    "SMTP_SERVIDOR",
    "SMTP_PUERTO",
    "EMAIL_REMITENTE",
    "CONTRASENA_APP",
    "ASUNTO",
}


def main():
    credenciales = cargar_credenciales()
    if not CLAVES_REQUERIDAS.issubset(credenciales.keys()):
        faltantes = CLAVES_REQUERIDAS - credenciales.keys()
        print(f"[Error] Faltan datos en credenciales.txt: {', '.join(faltantes)}")
        return

    cuerpo = cargar_presentacion()
    if not cuerpo:
        print("[Cancelado] El archivo presentacion.txt está vacío o no se pudo leer.")
        return

    datos_pdf = cargar_cv()
    if datos_pdf is None:
        print("[Cancelado] No se pudo cargar el archivo del CV.")
        return

    destinatarios = cargar_destinatarios()
    if not destinatarios:
        print("[Cancelado] No hay direcciones cargadas en destinatarios.txt.")
        return

    enviados_previos = {correo.lower() for correo in cargar_enviados()}

    # Filtrar ya enviados y evitar duplicados en la lista manteniendo el orden
    pendientes = []
    vistos = set()
    for correo in destinatarios:
        correo_norm = correo.lower()
        if correo_norm not in enviados_previos and correo_norm not in vistos:
            pendientes.append(correo)
            vistos.add(correo_norm)

    if not pendientes:
        print("Todos los correos de destinatarios.txt ya fueron enviados anteriormente.")
        return

    print(f"Iniciando envío de {len(pendientes)} correo(s) pendiente(s)...")
    total_enviados = enviar_tanda(
        credenciales=credenciales,
        destinatarios=pendientes,
        cuerpo=cuerpo,
        datos_pdf=datos_pdf,
        al_enviar=registrar_enviado,
    )
    print(f"Proceso finalizado. Enviados con éxito: {total_enviados}/{len(pendientes)}.")


if __name__ == "__main__":
    main()