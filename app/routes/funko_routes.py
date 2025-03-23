from flask import Blueprint, jsonify, request
from app.services.funko_services import get_funkos

funko_bp = Blueprint('funko_bp', __name__)

@funko_bp.route('/funko_pop', methods=['GET'])
def get_funkos_route():
    """Route pour récupérer les Funkos avec pagination."""
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        return jsonify(get_funkos(page, per_page)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
