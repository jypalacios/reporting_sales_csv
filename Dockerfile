# 1. Usar una imagen base oficial de Python ligera
FROM python:3.12-slim

# 2. Configurar variables de entorno para optimizar Python en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiar primero solo el archivo de requerimientos (aprovecha la caché de capas de Docker)
COPY requirements.txt .

# 5. Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar el resto del código fuente del proyecto
COPY . .

# 7. Informar el puerto en el que escuchará el contenedor (por defecto Flask usa el 5000)
#EXPOSE 5000

# 8. Comando para ejecutar la aplicación usando el servidor integrado de Flask
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python", "analisis.py"]

