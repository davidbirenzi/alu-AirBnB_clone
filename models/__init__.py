#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
