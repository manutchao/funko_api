from flask import Blueprint, jsonify
from app import mongo

api = Blueprint('api', __name__)

@api.route('/ping', methods=['GET'])
def ping():
    try:
        mongo.db.command("ping")
        return jsonify({"message": "MongoDB connection successful!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500