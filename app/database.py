# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Modificación de la URL de conexión
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Python1234@localhost:5432/biblioteca_db"

# Crear el motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear la sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()