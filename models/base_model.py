#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    __table_args__ = {
            'mysql_charset': 'latin1',
            'mysql_collate': 'latin1_swedish_ci'
             }

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "updated_at":
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if k == "created_at":
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                    continue
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dic = self.__dict__.copy()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return '[{}] ({}) {}'.format(cls, self.id, dic)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
        print("OK")

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del (dictionary["_sa_instance_state"])
        return dictionary

    def delete(self):
        """Delete from FileStorage endpoint"""
        models.storage.delete(self)
