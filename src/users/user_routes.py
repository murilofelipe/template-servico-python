# src/users/user_routes.py
from flask import Blueprint, jsonify, request
from pydantic import ValidationError

from users import user_controller
from users.user_schemas import UserInput

# Um Blueprint é uma forma de organizar um grupo de rotas relacionadas
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def get_users_route():
    users = user_controller.get_all_users()
    # Pydantic models precisam ser convertidos para dict para o jsonify
    return jsonify([user.model_dump() for user in users])


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id_route(user_id: int):
    user = user_controller.get_user_by_id(user_id)
    if user:
        return jsonify(user.model_dump())
    return jsonify({"error": "User not found"}), 404


@user_bp.route("/", methods=["POST"])
def create_user_route():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400
    try:
        user_input = UserInput(**data)
    except (ValidationError, TypeError) as e:
        return jsonify({"error": str(e)}), 400
    user = user_controller.create_user(user_input)
    return jsonify(user.model_dump()), 201
