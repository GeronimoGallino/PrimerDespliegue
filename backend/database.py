import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Obtener la URL de la base de datos desde las variables de entorno.
# Si no existe (estás en local), usa tu ruta de SQLite por defecto.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./backend/database.db")

# 2. Corrección de compatibilidad para Heroku/Render/Railway:
# A veces la URL viene como "postgres://" pero SQLAlchemy requiere "postgresql://"
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Configuración del motor (Engine)
# SQLite necesita "check_same_thread", pero PostgreSQL NO.
connect_args = {}
if "sqlite" in DATABASE_URL:
    connect_args = {"check_same_thread": False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

# Creador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()

# Dependencia que se usará en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()