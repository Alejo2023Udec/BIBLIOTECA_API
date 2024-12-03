from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError  # Importamos excepciones de SQLAlchemy
from . import models, schemas

# Función para listar todos los libros
def listar_libros(db: Session):
    try:
        # Retorna todos los libros desde la base de datos
        return db.query(models.Libro).all()
    except SQLAlchemyError as e:
        # Si ocurre un error en la consulta, lo capturamos y retornamos el error
        print(f"Error al listar libros: {e}")
        return None

# Función para agregar un nuevo libro
def agregar_libro(db: Session, libro: schemas.LibroCreate):
    try:
        # Crea una instancia de Libro a partir de los datos proporcionados
        db_libro = models.Libro(
            titulo=libro.titulo,
            autor=libro.autor,
            año_publicacion=libro.año_publicacion,  # Asegúrate de que 'año_publicacion' está bien definido en tu modelo
            isbn=libro.isbn
        )
        db.add(db_libro)
        db.commit()
        db.refresh(db_libro)
        return db_libro
    except SQLAlchemyError as e:
        # Si ocurre un error al agregar el libro, lo capturamos y retornamos el error
        db.rollback()  # Hacemos un rollback si hay error
        print(f"Error al agregar libro: {e}")
        return None

# Función para obtener un libro por su ID
def obtener_libro(db: Session, libro_id: int):
    try:
        # Busca el libro por su ID y lo retorna
        return db.query(models.Libro).filter(models.Libro.id == libro_id).first()
    except SQLAlchemyError as e:
        # Si ocurre un error en la consulta, lo capturamos y retornamos el error
        print(f"Error al obtener libro con ID {libro_id}: {e}")
        return None

# Función para actualizar un libro
def actualizar_libro(db: Session, libro_id: int, libro: schemas.LibroUpdate):
    try:
        # Busca el libro por su ID
        db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
        
        # Si no se encuentra el libro, retorna None
        if db_libro is None:
            return None
        
        # Si se proporciona un nuevo valor, actualiza el libro
        if libro.titulo:
            db_libro.titulo = libro.titulo
        if libro.autor:
            db_libro.autor = libro.autor
        if libro.año_publicacion:
            db_libro.año_publicacion = libro.año_publicacion
        if libro.isbn:
            db_libro.isbn = libro.isbn
        
        db.commit()
        db.refresh(db_libro)
        return db_libro
    except SQLAlchemyError as e:
        # Si ocurre un error al actualizar el libro, lo capturamos y retornamos el error
        db.rollback()  # Hacemos un rollback si hay error
        print(f"Error al actualizar libro con ID {libro_id}: {e}")
        return None

# Función para eliminar un libro
def eliminar_libro(db: Session, libro_id: int):
    try:
        # Busca el libro por su ID
        db_libro = db.query(models.Libro).filter(models.Libro.id == libro_id).first()
        
        # Si no se encuentra el libro, retorna None
        if db_libro is None:
            return None
        
        # Elimina el libro encontrado
        db.delete(db_libro)
        db.commit()
        return db_libro
    except SQLAlchemyError as e:
        # Si ocurre un error al eliminar el libro, lo capturamos y retornamos el error
        db.rollback()  # Hacemos un rollback si hay error
        print(f"Error al eliminar libro con ID {libro_id}: {e}")
        return None
