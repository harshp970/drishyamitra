from flask import Blueprint, jsonify

face_bp = Blueprint('face_bp', __name__)

@face_bp.route('/test', methods=['GET'])
def test_face():
    return jsonify({"message": "Face route working"})
