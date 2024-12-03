# app/schemas.py

from pydantic import BaseModel

# Esquema para la creación de un libro
class LibroCreate(BaseModel):
    titulo: str
    autor: str
    año: int
    isbn: str

    class Config:
        from_attributes = True  # Cambio de 'orm_mode' a 'from_attributes'


# Esquema para actualizar un libro (solo los campos que se desean actualizar)
class LibroUpdate(BaseModel):
    titulo: str | None = None
    autor: str | None = None
    año: int | None = None
    isbn: str | None = None

    class Config:
        from_attributes = True  # Cambio de 'orm_mode' a 'from_attributes'


# Esquema para mostrar los detalles de un libro
class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    año: int
    isbn: str

    class Config:
        from_attributes = True  # Cambio de 'orm_mode' a 'from_attributes'














