<<<<<<< HEAD
# Usa la imagen oficial de Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
=======
# BIBLIOTECA_API
>>>>>>> 04114f7d6bb8ac5daf6d67b327140d9b167b6bf4
