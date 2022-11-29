#!/usr/bin/python3
"""Creates an instance of FileStoarage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
