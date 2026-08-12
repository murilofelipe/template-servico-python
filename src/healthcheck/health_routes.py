# src/healthcheck/health_routes.py
from flask import Blueprint, jsonify
from sqlalchemy import text

from database import db

health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/health")
def health():
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "ok", "database": "connected"}), 200
    except Exception:
        return jsonify({"status": "unhealthy", "database": "disconnected"}), 503
