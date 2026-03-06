from flask import Blueprint, jsonify

delivery_bp = Blueprint("delivery_bp", __name__)

@delivery_bp.route("/test")
def test_delivery():
    return jsonify({"message": "Delivery route working"})