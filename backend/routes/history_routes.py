from flask import Blueprint, jsonify

history_bp = Blueprint("history_bp", __name__)

@history_bp.route("/test")
def test_history():
    return jsonify({"message": "History route working"})