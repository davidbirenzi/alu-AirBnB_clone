#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

def __init__(self, *args, **kwargs):
    """initialize the data model"""
    super().__init__(*args, **kwargs)
