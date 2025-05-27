from flask import Blueprint, request, jsonify
from app.services.user_service import create_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    result = create_user(data)
    return jsonify(result)

