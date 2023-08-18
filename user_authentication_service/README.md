# User Authentication Service

This project is aimed at creating a user authentication service using Flask, SQLAlchemy, and bcrypt. The service allows users to register, log in, log out, reset passwords, and view their profile.

## Getting Started

To get started, follow these steps:

1. Clone this repository:
git clone https://github.com/your-username/alx-backend-user-data.git

cd alx-backend-user-data/0x03-user_authentication_service

2. Install the required dependencies:
pip3 install -r requirements.txt


3. Run the Flask app:
python app.py

## Tasks Overview

### 0. User Model

- Define the SQLAlchemy model named `User` with attributes `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

### 1. Create User

- Implement the `add_user` method in the `DB` class to add a new user to the database.

### 2. Find User

- Implement the `find_user_by` method in the `DB` class to find a user by given attributes.

### 3. Update User

- Implement the `update_user` method in the `DB` class to update user attributes.

### 4. Hash Password

- Define a `_hash_password` function in the `auth` module to hash passwords using bcrypt.

### 5. Register User

- Implement the `register_user` method in the `Auth` class to register users and store hashed passwords.

### 6. Basic Flask App

- Set up a basic Flask app with a single route that returns a JSON message.

### 7. Register User (API Endpoint)

- Implement the API endpoint `/users` to register users via a POST request.

### 8. Credentials Validation

- Implement the `valid_login` method in the `Auth` class to validate user credentials.

### 9. Generate UUIDs

- Define a private `_generate_uuid` function in the `auth` module to generate UUIDs.

### 10. Get Session ID

- Implement the `create_session` method in the `Auth` class to create a session for a user.

### 11. Log In (API Endpoint)

- Implement the API endpoint `/sessions` to log in users via a POST request.

### 12. Find User by Session ID

- Implement the `get_user_from_session_id` method in the `Auth` class to retrieve users by session ID.

### 13. Destroy Session

- Implement the `destroy_session` method in the `Auth` class to destroy user sessions.

### 14. Log Out (API Endpoint)

- Implement the API endpoint `/sessions` to log out users via a DELETE request.

### 15. User Profile (API Endpoint)

- Implement the API endpoint `/profile` to retrieve user profiles via a GET request.

### 16. Generate Reset Password Token

- Implement the `get_reset_password_token` method in the `Auth` class to generate reset password tokens.

### 17. Get Reset Password Token (API Endpoint)

- Implement the API endpoint `/reset_password` to get reset password tokens via a POST request.

### 18. Update Password

- Implement the `update_password` method in the `Auth` class to update passwords.

### 19. Update Password (API Endpoint)

- Implement the API endpoint `/reset_password` to update passwords via a PUT request.

### 20. End-to-end Integration Test

- Create a `main.py` module to perform end-to-end integration tests for different actions.

## Contributors

- [Your Name](https://github.com/your-username)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


3. Run the Flask app:

python3 app.py


## Tasks Overview

### 0. User Model

- Define the SQLAlchemy model named `User` with attributes `id`, `email`, `hashed_password`, `session_id`, and `reset_token`.

### 1. Create User

- Implement the `add_user` method in the `DB` class to add a new user to the database.

### 2. Find User

- Implement the `find_user_by` method in the `DB` class to find a user by given attributes.

### 3. Update User

- Implement the `update_user` method in the `DB` class to update user attributes.

### 4. Hash Password

- Define a `_hash_password` function in the `auth` module to hash passwords using bcrypt.

### 5. Register User

- Implement the `register_user` method in the `Auth` class to register users and store hashed passwords.

### 6. Basic Flask App

- Set up a basic Flask app with a single route that returns a JSON message.

### 7. Register User (API Endpoint)

- Implement the API endpoint `/users` to register users via a POST request.

### 8. Credentials Validation

- Implement the `valid_login` method in the `Auth` class to validate user credentials.

### 9. Generate UUIDs

- Define a private `_generate_uuid` function in the `auth` module to generate UUIDs.

### 10. Get Session ID

- Implement the `create_session` method in the `Auth` class to create a session for a user.

### 11. Log In (API Endpoint)

- Implement the API endpoint `/sessions` to log in users via a POST request.

### 12. Find User by Session ID

- Implement the `get_user_from_session_id` method in the `Auth` class to retrieve users by session ID.

### 13. Destroy Session

- Implement the `destroy_session` method in the `Auth` class to destroy user sessions.

### 14. Log Out (API Endpoint)

- Implement the API endpoint `/sessions` to log out users via a DELETE request.

### 15. User Profile (API Endpoint)

- Implement the API endpoint `/profile` to retrieve user profiles via a GET request.

### 16. Generate Reset Password Token

- Implement the `get_reset_password_token` method in the `Auth` class to generate reset password tokens.

### 17. Get Reset Password Token (API Endpoint)

- Implement the API endpoint `/reset_password` to get reset password tokens via a POST request.

### 18. Update Password

- Implement the `update_password` method in the `Auth` class to update passwords.

### 19. Update Password (API Endpoint)

- Implement the API endpoint `/reset_password` to update passwords via a PUT request.

### 20. End-to-end Integration Test

- Create a `main.py` module to perform end-to-end integration tests for different actions.

## Contributors

- [Nwodo Thomas](https://github.com/Nwodothomas)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




