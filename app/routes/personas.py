import json
import time
import requests
from flask import Blueprint, jsonify, request
from app.config import Config
from app.database import get_couch_headers

personas_bp = Blueprint("personas", __name__, url_prefix="/api/personas")


@personas_bp.route("", methods=["GET"])
def get_personas():
    try:
        response = requests.get(
            f"{Config.COUCHDB_URL}/personal/_all_docs?include_docs=true",
            headers=get_couch_headers(),
            timeout=5,
        )
        response.raise_for_status()
        data = response.json()
        docs = []
        for row in data.get("rows", []):
            doc = row.get("doc") or {}
            if doc.get("tipo") == "persona":
                docs.append({
                    "id": doc.get("_id"),
                    "nombre": doc.get("nombre"),
                    "apellido": doc.get("apellido"),
                    "dni": doc.get("dni"),
                })
        return jsonify(docs)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@personas_bp.route("", methods=["POST"])
def create_persona():
    payload = request.get_json(silent=True) or {}
    timestamp = int(time.time())
    doc_id = payload.get("_id") or f"persona_{payload.get('dni', 'nuevo')}_{timestamp}"
    body = {
        "_id": doc_id,
        "tipo": "persona",
        "nombre": payload.get("nombre", ""),
        "apellido": payload.get("apellido", ""),
        "dni": payload.get("dni", ""),
    }

    try:
        response = requests.put(
            f"{Config.COUCHDB_URL}/personal/{doc_id}",
            headers=get_couch_headers(),
            data=json.dumps(body),
            timeout=5,
        )
        response.raise_for_status()
        return jsonify({"ok": True, "id": doc_id})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500
