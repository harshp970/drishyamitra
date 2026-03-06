from flask import Blueprint, jsonify

chat_bp = Blueprint("chat_bp", __name__)

@chat_bp.route("/test")
def test_chat():
    return jsonify({"message": "Chat route working"})