# src/users/user_routes.py
from flask import Blueprint, jsonify
from . import user_controller

# Um Blueprint é uma forma de organizar um grupo de rotas relacionadas
user_bp = Blueprint("user_bp", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def get_users_route():
    users = user_controller.get_all_users()
    # Pydantic models precisam ser convertidos para dict para o jsonify
    return jsonify([user.dict() for user in users])


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id_route(user_id: int):
    user = user_controller.get_user_by_id(user_id)
    if user:
        return jsonify(user.dict())
    return jsonify({"error": "User not found"}), 404
