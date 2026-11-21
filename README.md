# Automatizador de Envío de Correos con Adjunto (Python)

Herramienta modular escrita en Python para automatizar el envío de correos electrónicos personalizados con un archivo PDF adjunto, orientada a procesos de postulación laboral. Desarrollada íntegramente con la biblioteca estándar de Python (`smtplib`, `email`, `pathlib`, `time`), sin dependencias externas.

## Características principales

- **Arquitectura modular:** Separación clara entre la lectura/escritura de archivos (`cargadores.py`), la gestión de conexión SMTP y armado de mensajes (`enviador.py`) y la lógica de control (`main.py`).
- **Control de duplicados:** Filtra automáticamente direcciones repetidas y cruza la lista de destinatarios contra un registro histórico (`enviados.txt`) para evitar reenviar correos a contactos ya gestionados.
- **Registro en tiempo real:** Cada dirección se guarda en el historial inmediatamente después de confirmarse su envío.
- **Validación previa:** Verifica que existan todas las claves de configuración y archivos necesarios antes de abrir la sesión con el servidor de correo.
- **Conexión segura:** Utiliza cifrado `STARTTLS` e intervalos de pausa entre envíos.

## Estructura del proyecto

```text
├── main.py              # Punto de entrada, validaciones y filtrado de duplicados
├── cargadores.py        # Lectura de archivos locales y registro de enviados
├── enviador.py          # Construcción del mensaje MIME y conexión SMTP
├── .gitignore           # Exclusión de credenciales y datos sensibles
└── README.md            # Documentación del proyecto