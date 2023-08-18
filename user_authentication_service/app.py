#!/usr/bin/env python3
"""
Basic Flask app with user registration, login, logout, profile, reset password, and update password endpoints
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()

@app.route("/")
def welcome():
    """GET route to return a JSON payload"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=["POST"])
def register_user():
    """Register a new user"""
    try:
        email = request.form["email"]
        password = request.form["password"]
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

@app.route("/sessions", methods=["POST"])
def login():
    """Login a user"""
    email = request.form["email"]
    password = request.form["password"]

    try:
        user = AUTH.login(email, password)
        response = make_response(jsonify({"email": email, "message": "logged in"}), 200)
        response.set_cookie("session_id", user.session_id)
        return response
    except ValueError:
        abort(401)

@app.route("/sessions", methods=["DELETE"])
def logout():
    """Logout a user"""
    session_id = request.cookies.get("session_id")
    
    try:
        AUTH.logout(session_id)
        return redirect("/")
    except ValueError:
        abort(403)

@app.route("/profile", methods=["GET"])
def profile():
    """Get user profile"""
    session_id = request.cookies.get("session_id")

    try:
        user = AUTH.get_user_from_session_id(session_id)
        return jsonify({"email": user.email}), 200
    except ValueError:
        abort(403)

@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """Get reset password token"""
    email = request.form["email"]

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)

@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Update user password using reset token"""
    email = request.form["email"]
    reset_token = request.form["reset_token"]
    new_password = request.form["new_password"]

    try:
        AUTH.update_password(email, reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
