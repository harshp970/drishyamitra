from flask import Blueprint, jsonify

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/test")
def test_auth():
    return jsonify({"message": "Auth route working"})