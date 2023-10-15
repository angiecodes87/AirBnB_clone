#!/usr/bin/python3
"""
BaseModel defines common attributes and methods for other classes.
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ Initializes, updates, and serializes objects """
    def __init__(self, *args, **kwargs):
        """ Initializes instance attributes """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)


def __str__(self):
    """ Returns a friendly object representation """
    return "[{}] ({}) {}".format(self.__class__.__name__,
                                 self.id, self.__dict__)


def save(self):
    """ Updates the 'updated_at' attribute """
    self.updated_at = datetime.today()
    storage.save()


def to_dict(self):
    """ Generates a dictionary representation with class information """
    new_dict = self.__dict__.copy()
    new_dict["__class__"] = self.__class__.__name__
    new_dict["created_at"] = self.created_at.isoformat()
    new_dict["updated_at"] = self.updated_at.isoformat()
    return new_dict
