from flask import Blueprint
from src.controllers.book_controller import *


book_bp = Blueprint('books', __name__)

# Get a book all books
@book_bp.route('/books', methods=['GET'])
def get_all_books():
    return get_all_books_controller(id)
    

# Create a new book
@book_bp.route('/books', methods=['POST'])
def create_book():
    return create_book_controller()

# Get a book by ID
@book_bp.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    return get_by_id_book_controller(id)

# Update a book by ID
@book_bp.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    return update_book_controller(id)

# Delete a book by ID (soft delete)
@book_bp.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    return delete_book_controller(id)

