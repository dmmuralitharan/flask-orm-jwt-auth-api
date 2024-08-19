from flask import Blueprint
from src.controllers.book_controller import *
from src.utils.jwt_token_utils import token_required

book_bp = Blueprint('books', __name__)

# Get a book all books
@book_bp.route('', methods=['GET'])
@token_required
def get_all_books(current_user, role):
    if role != 'user':
        return jsonify({'message': 'Permission denied', "success": 0}), 403
    return get_all_books_controller(current_user)
    

# Create a new book
@book_bp.route('', methods=['POST'])
@token_required
def create_book(current_user, role):
    if role != 'user':
        return jsonify({'message': 'Permission denied', "success": 0}), 403
    return create_book_controller(current_user)

# Get a book by ID
@book_bp.route('/<int:id>', methods=['GET'])
@token_required
def get_book(id, current_user, role):
    if role != 'user':
        return jsonify({'message': 'Permission denied', "success": 0}), 403
    return get_by_id_book_controller(id, current_user)

# Update a book by ID
@book_bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_book(id, current_user, role):
    if role != 'user':
        return jsonify({'message': 'Permission denied', "success": 0}), 403
    return update_book_controller(id=id, current_user=current_user)

# Delete a book by ID
@book_bp.route('/<int:id>', methods=['DELETE'])
@token_required
def delete_book(id, current_user, role):
    if role != 'user':
        return jsonify({'message': 'Permission denied', "success": 0}), 403
    return delete_book_controller(id=id, current_user=current_user)

