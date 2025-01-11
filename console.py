#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage

# List of valid classes
classes = {"BaseModel": BaseModel}
