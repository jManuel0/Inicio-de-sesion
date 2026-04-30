# Despliegue en Render

Este proyecto ya incluye los archivos necesarios para desplegar en Render:

- `requirements.txt`: dependencias de produccion.
- `build.sh`: instala dependencias, recopila estaticos y ejecuta migraciones.
- `render.yaml`: blueprint con Web Service y PostgreSQL.
- `.python-version`: fija Python 3.13.5.

## Opcion recomendada: Blueprint

1. Sube los cambios a GitHub.
2. En Render, entra a **Blueprints**.
3. Selecciona **New Blueprint Instance**.
4. Conecta el repositorio.
5. Render detectara `render.yaml`.
6. Aplica el blueprint.

Render creara:

- Un Web Service llamado `calificaciones-django`.
- Una base de datos PostgreSQL llamada `calificaciones-db`.
- Variables de entorno para `DATABASE_URL`, `SECRET_KEY`, `WEB_CONCURRENCY` y `PYTHON_VERSION`.

## Opcion manual

Si prefieres crear el servicio manualmente:

1. Crea una base de datos PostgreSQL en Render.
2. Crea un Web Service conectado al repositorio.
3. Usa estos comandos:

```bash
bash build.sh
```

```bash
cd evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez && python -m gunicorn evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez.wsgi:application --bind 0.0.0.0:$PORT
```

4. Agrega estas variables:

```text
DATABASE_URL=<Internal Database URL de Render PostgreSQL>
SECRET_KEY=<generada por Render>
WEB_CONCURRENCY=4
PYTHON_VERSION=3.13.5
```

## Crear usuario administrador

Cuando el deploy termine, abre la Shell del servicio en Render y ejecuta:

```bash
cd evaluaciones_juan_manuel_miguel_alfaro_carlos_taquez
python manage.py createsuperuser
```

## Notas

- En local, si no existe `DATABASE_URL`, Django usa SQLite.
- En Render, si existe `DATABASE_URL`, Django usa PostgreSQL.
- `DEBUG` queda en `False` automaticamente en Render.
