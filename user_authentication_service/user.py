#!/usr/bin/env python3
"""
User module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class for database table 'users'
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: str = None, reset_token: str = None) -> None:
        """
        Initializes a User object.
        """
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

# Additional methods and functionality specific to the User class can be added here.
