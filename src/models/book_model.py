from src import db

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, server_default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    delete_status = db.Column(db.Boolean, default=True)