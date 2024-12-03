
# Biblioteca API

Biblioteca API es un proyecto desarrollado con **FastAPI** que proporciona funcionalidades para gestionar libros, incluyendo la capacidad de listar, agregar, actualizar y eliminar libros. Además, permite la conexión a una base de datos PostgreSQL para almacenar la información.

## Instalación

Clonar este repositorio:
   ```bash
   git clone https://github.com/Alejo2023Udec/BIBLIOTECA_API.git
   cd BIBLIOTECA_API
Configura un entorno virtual:

python -m venv env
source env/bin/activate   # En Windows usa: .\env\Scripts\activate
Instala las dependencias:

pip install -r requirements.txt
Configura la base de datos PostgreSQL:

Crea una base de datos llamada biblioteca_db.
Ajusta la configuración en el archivo app/database.py:
SQLALCHEMY_DATABASE_URL = "postgresql://<usuario>:<contraseña>@localhost:5432/biblioteca_db"
Inicia las migraciones de la base de datos:

python -m app.database
Uso
Inicia el servidor:

uvicorn app.main:app --reload
Accede a la documentación interactiva en:

http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
Funcionalidades de la API
Endpoints principales
GET /libros: Lista todos los libros.
POST /libros: Agrega un nuevo libro.
GET /libros/{id}: Obtiene un libro por su ID.
PUT /libros/{id}: Actualiza un libro existente.
DELETE /libros/{id}: Elimina un libro.
Ejemplo de un libro
{
  "id": 1,
  "titulo": "El Quijote",
  "autor": "Miguel de Cervantes",
  "año": 1605,
  "isbn": "1234567890"
}
Pruebas
Ejecuta los tests con Pytest:

pytest
Docker
Construye la imagen:

docker build -t biblioteca-api .
Ejecuta el contenedor:

docker run -d -p 8000:8000 biblioteca-api
Seguridad
La API utiliza técnicas para prevenir vulnerabilidades:

Protección contra inyección SQL mediante el uso de un ORM (SQLAlchemy).
Validación de datos con Pydantic.
Cifrado de tráfico mediante HTTPS.
Límites de solicitudes para evitar ataques DDoS.
Escalabilidad
Esta API puede ser escalada utilizando Docker para contenerización y Kubernetes para orquestación, balanceadores de carga, y caché con Redis para optimizar el rendimiento.







RESPUESTAS 

Autenticación y autorización: Implementaría autenticación basada en JWT (JSON Web Tokens) para manejar sesiones de usuario de manera segura, utilizando OAuth2 para flujos de inicio de sesión y asignación de roles como usuario y administrador para controlar el acceso a los recursos.

Estrategias de escalabilidad: Escalaría la aplicación horizontalmente mediante contenedores Docker orquestados con Kubernetes, distribuyendo el tráfico con balanceadores de carga y optimizando consultas de base de datos mediante índices, sharding y caché con Redis para respuestas rápidas.

Paginación en endpoints: Usaría parámetros como ?page=1&size=10 en las consultas y aplicaría LIMIT y OFFSET en las bases de datos para limitar los resultados devueltos, agregando metadatos en las respuestas para facilitar la navegación.

Seguridad de la aplicación: Prevendría inyecciones SQL utilizando un ORM como SQLAlchemy y validando las entradas con Pydantic, protegería contra XSS con sanitización y cabeceras de seguridad, implementaría HTTPS para encriptar el tráfico y usaría rate-limiting para prevenir abusos.






