#!/usr/bin/python3
"""
DATA BASE STORAGE ENGINE
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBstorage:
    """Data Base Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Engine Variable"""
        usr = os.getenv('HBNB_MYSQL_USER')
        pd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        eng_string = f"mysql+mysqldb://{usr}:{pd}@{host}:3306/{db}"

        DBstorage.__engine = create_engine(eng_string, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.reflect(bind=DBstorage.__engine)
            metadata.drop_all(bind=DBstorage.__engine)

    def all(self, cls=None):
        """Return Data from Database According to class"""
        data = {}
        if cls is None:
            classes = [State, City, User, Place, User]
            q_obj = []
            for cl in classes:
                q_obj += DBstorage.__session.query(cl).all()
        else:
            q_obj = DBstorage.__session.query(cls).all()

        for obj in q_obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            data[key] = obj

        return data

    def new(self, obj):
        """Add object to data Base"""
        DBstorage.__session.add(obj)

    def save(self):
        """save after adding"""
        DBstorage.__session.commit()

    def delete(self, obj=None):
        """Delete from data base"""
        if obj is None:
            DBstorage.__session.delete(obj)
            DBstorage.__session.commit()

    def reload(self):
        """Intial Reloading"""
        Base.metadata.create_all(DBstorage.__engine)
        Session = sessionmaker(bind=DBstorage.__engine, expire_on_commit=False)
        DBstorage.__session = scoped_session(Session)
