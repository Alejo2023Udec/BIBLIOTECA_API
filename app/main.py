from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db

# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Ruta raíz para verificar si la API está funcionando
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de la biblioteca"}

# Ruta para listar todos los libros
@app.get("/libros", response_model=list[schemas.Libro])
def listar_libros(db: Session = Depends(get_db)):
    try:
        libros = crud.listar_libros(db)
        if libros is None:
            raise HTTPException(status_code=500, detail="Error al obtener los libros")
        return libros
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para agregar un nuevo libro
@app.post("/libros", response_model=schemas.Libro)
def agregar_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    try:
        nuevo_libro = crud.agregar_libro(db, libro)
        if nuevo_libro is None:
            raise HTTPException(status_code=500, detail="Error al agregar el libro")
        return nuevo_libro
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para obtener un libro por su ID
@app.get("/libros/{libro_id}", response_model=schemas.Libro)
def obtener_libro(libro_id: int, db: Session = Depends(get_db)):
    try:
        db_libro = crud.obtener_libro(db, libro_id)
        if db_libro is None:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return db_libro
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para actualizar un libro
@app.put("/libros/{libro_id}", response_model=schemas.Libro)
def actualizar_libro(libro_id: int, libro: schemas.LibroUpdate, db: Session = Depends(get_db)):
    try:
        db_libro = crud.actualizar_libro(db, libro_id, libro)
        if db_libro is None:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return db_libro
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para eliminar un libro
@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int, db: Session = Depends(get_db)):
    try:
        db_libro = crud.eliminar_libro(db, libro_id)
        if db_libro is None:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return {"message": "Libro eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
