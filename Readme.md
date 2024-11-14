# Event service

## Variables de Entorno
| **Nombre**                | **Descripción**                                                          | **Default**                                                   |
| ------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------- |
| `KAFKA_SERVER`            | Servidor de Kafka para la conexión.                                      | ``                                                            |
| `KAFKA_GROUP`             | Grupo de consumidores de Kafka.                                          | ``                                                            |
| `KAFKA_TOPIC`             | Topico o topicos de Kafka para recibir mensajes de imágenes a procesar.  | ``                                                            |
| `MINIO_HOST`              | Host del servidor MinIO.                                                 | ``                                                            |
| `MINIO_ACCESS_KEY`        | Clave de acceso para el servidor MinIO.                                  | ``                                                            |
| `MINIO_SECRET_KEY`        | Clave secreta para el servidor MinIO.                                    | ``                                                            |
| `MINIO_SECURE`            | Indica si la conexión con MinIO debe ser segura (HTTPS).                 | ``                                                            |
| `MINIO_CERT_CHECK`        | Indica si se debe verificar el certificado SSL de MinIO.                 | ``                                                            |
| `REDIS_HOST`              | Host del servidor Redis.                                                 | ``                                                            |
| `REDIS_PORT`              | Puerto del servidor Redis.                                               | ``                                                            |
| `SENTRY_DSN`              | DSN de Sentry para el monitoreo de errores.                              | ``                                                            |

## Ejecución del Proyecto

Para ejecutar el proyecto sigue estos pasos:

### 1. Configura las Variables de Entorno

1. **Crea un archivo `.env`** basado en el archivo de ejemplo `.env.sample` que se encuentra en el repositorio. Este archivo contiene las variables de entorno necesarias para configurar el proyecto.

    ```bash
    cp .env.sample .env
    ```

2. **Edita el archivo `.env`** para establecer las variables de entorno adecuadas. Asegúrate de proporcionar valores correctos para todas las variables. Puedes usar cualquier editor de texto para editar el archivo.

    ```ini
    # Kafka
    KAFKA_SERVER=
    KAFKA_GROUP=
    KAFKA_TOPIC=

    # Minio
    MINIO_HOST=
    MINIO_ACCESS_KEY=
    MINIO_SECRET_KEY=
    MINIO_SECURE=
    MINIO_CERT_CHECK=

    # Redis
    REDIS_HOST=
    REDIS_PORT=

    # Sentry
    SENTRY_DSN=
    ```

### 2. Ejecuta el Proyecto

1. **Usa Docker Compose para levantar el contenedor.** Asegúrate de que Docker y Docker Compose estén instalados en tu máquina.

    ```bash
    docker-compose up
    ```

    Este comando ejecutará el contenedor con la configuración definida en `docker-compose.yml`, usando el archivo `.env` para las variables de entorno.

### Notas Adicionales

- Si deseas ejecutar el contenedor en segundo plano, añade la opción `-d` al comando de Docker Compose:

    ```bash
    docker-compose up -d
    ```

- Para detener el contenedor, puedes usar:

    ```bash
    docker-compose down
    ```