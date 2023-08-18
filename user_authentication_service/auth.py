#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
import uuid
from user import User
from db import DB

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hashes a password and returns the salted hash as bytes"""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def _generate_uuid(self) -> str:
        """Generates a string representation of a new UUID"""
        return str(uuid.uuid4())

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user"""

        # Check if the user already exists
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except ValueError:
            pass  # User not found, continue with registration

        # Hash the password
        hashed_password = self._hash_password(password)

        # Add the user to the database
        new_user = self._db.add_user(email, hashed_password)

        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user credentials"""

        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8'))
        except ValueError:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session for the user and returns the session ID"""

        user = self._db.find_user_by(email=email)
        session_id = self._generate_uuid()
        user.session_id = session_id
        self._db._session.commit()

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """Returns the corresponding User or None for a given session ID"""
        
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except ValueError:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session of the corresponding user"""
        user = self._db.find_user_by(id=user_id)
        user.session_id = None
        self._db._session.commit()

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset password token and returns it"""
        user = self._db.find_user_by(email=email)
        reset_token = self._generate_uuid()
        user.reset_token = reset_token
        self._db._session.commit()
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates user's password based on reset_token"""
        user = self._db.find_user_by(reset_token=reset_token)
        if user is None:
            raise ValueError("Invalid reset token")
        
        hashed_password = self._hash_password(password)
        user.hashed_password = hashed_password
        user.reset_token = None
        self._db._session.commit()
