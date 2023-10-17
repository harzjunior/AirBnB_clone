#!/usr/bin/python3
"""
This module executes automatically when the 'models' package is imported.
"""


from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
