# Imagen oficial liviana de Python 3.11
FROM python:3.11-slim

# Evita la generación de archivos .pyc y fuerza el stdout/stderr inmediato para logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos e instalamos dependencias primero para aprovechar el sistema de capas de Docker (Caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código completo de la aplicación
COPY . .

# Puerto expuesto por Flask / Gunicorn
EXPOSE 5000

# En producción (TrueNAS/Docker) usamos Gunicorn como servidor WSGI profesional
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:create_app()"]
