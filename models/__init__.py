#!/usr/bin/python3
""" Initialize the FileStorage class """

from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Load data from the storage file
storage.reload()
