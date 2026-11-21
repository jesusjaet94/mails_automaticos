from email.message import EmailMessage
import smtplib
import time


def armar_correo(remitente, destinatario, asunto, cuerpo, datos_pdf, nombre_pdf):
    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = remitente
    msg["To"] = destinatario
    msg.set_content(cuerpo, subtype="plain", charset="utf-8")

    msg.add_attachment(
        datos_pdf,
        maintype="application",
        subtype="pdf",
        filename=nombre_pdf,
    )
    return msg


def enviar_tanda(
    credenciales,
    destinatarios,
    cuerpo,
    datos_pdf,
    nombre_pdf="cv.pdf",
    al_enviar=None,
    pausa=3,
):
    servidor_smtp = credenciales["SMTP_SERVIDOR"]
    puerto = int(credenciales["SMTP_PUERTO"])
    remitente = credenciales["EMAIL_REMITENTE"]
    contrasena = credenciales["CONTRASENA_APP"]
    asunto = credenciales["ASUNTO"]

    enviados_ok = 0

    try:
        with smtplib.SMTP(servidor_smtp, puerto) as servidor:
            servidor.starttls()
            servidor.login(remitente, contrasena)

            for indice, destinatario in enumerate(destinatarios, start=1):
                correo = armar_correo(
                    remitente=remitente,
                    destinatario=destinatario,
                    asunto=asunto,
                    cuerpo=cuerpo,
                    datos_pdf=datos_pdf,
                    nombre_pdf=nombre_pdf,
                )
                try:
                    servidor.send_message(correo)
                    enviados_ok += 1
                    print(f"[{indice}/{len(destinatarios)}] Enviado a: {destinatario}")

                    if al_enviar:
                        al_enviar(destinatario)

                except smtplib.SMTPException as error:
                    print(f"[Error] No se pudo enviar a {destinatario}: {error}")

                if indice < len(destinatarios):
                    time.sleep(pausa)

    except smtplib.SMTPAuthenticationError:
        print("[Error crítico] Falló el inicio de sesión. Revisa EMAIL_REMITENTE y CONTRASENA_APP en credenciales.txt.")
    except Exception as error:
        print(f"[Error crítico] Problema de conexión con el servidor SMTP: {error}")

    return enviados_ok