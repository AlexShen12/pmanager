#external 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Internal 
from .config import settings

SQLALCHEMY_db_url = settings.DATABASE_URL

engine = create_engine(
    SQLALCHEMY_db_url, 
    connect_args={"check_same_thread": False}
)

Session = sessionmaker(
    autocommit = False,
    autoflush= False,
    bind = engine
)

def get_db():
    db = Session()
    try: 
        yield db
    finally:
        db.close()
















    