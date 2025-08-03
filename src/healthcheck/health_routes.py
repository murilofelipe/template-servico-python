# src/healthcheck/health_routes.py
from flask import Blueprint, jsonify

health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/health")
def health():
    return jsonify({"status": "ok"})
