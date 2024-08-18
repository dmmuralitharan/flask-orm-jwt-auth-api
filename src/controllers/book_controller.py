from flask import jsonify, request
from src import db
from src.models.book_model import Book

def get_all_books_controller():
    try:
        books = Book.query.filter(Book.delete_status == 1).all()
        books_list = [{
            'id': book.id,
            'book_name': book.book_name,
            'price': book.price,
            'date_created': book.date_created,
            'date_modified': book.date_modified,
            'delete_status': book.delete_status
        } for book in books]
        return jsonify(books_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_book_controller():
    try:
        data = request.get_json()
        
        book = Book(
            book_name=data['book_name'],
            price=data['price'],
        )
        db.session.add(book)
        db.session.commit()
        return jsonify({'message': 'Book created successfully', 'book': book.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

def get_by_id_book_controller(id):
    try:
        book = Book.query.filter(Book.id == id, Book.delete_status == 1).first()
        return jsonify({
            'id': book.id,
            'book_name': book.book_name,
            'price': book.price,
            'date_created': book.date_created,
            'date_modified': book.date_modified,
            'delete_status': book.delete_status
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_book_controller(id):
    try:
        data = request.get_json()
        book = Book.query.get_or_404(id)
        if 'book_name' in data:
            book.book_name = data['book_name']
        if 'price' in data:
            book.price = data['price']
        if 'delete_status' in data:
            book.delete_status = data['delete_status']
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

def delete_book_controller(id):
    try:
        book = Book.query.get_or_404(id)
        book.delete_status = False
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

