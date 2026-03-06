from flask import Blueprint, jsonify

photo_bp = Blueprint("photo_bp", __name__)

@photo_bp.route("/test")
def test_photo():
    return jsonify({"message": "Photo route working"})