from flask import Blueprint, jsonify

edit_bp = Blueprint("edit_bp", __name__)

@edit_bp.route("/test")
def test_edit():
    return jsonify({"message": "Edit route working"})