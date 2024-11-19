from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import Base
from .config import Config

engine = create_engine(Config.DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Base.metadata.create_all(bind=engine)
    return app
