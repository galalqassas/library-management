from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
books = []


@app.route('/')
def welcome():
    return "<h1> Welcome </h1>"

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    required_fields = ['title', 'author', 'published_year', 'isbn']

    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields'}), 400

    isbn = data.get('isbn')
    if any(book['isbn'] == isbn for book in books):
        return jsonify({'message': f'Book with ISBN {isbn} already exists'}), 400

    books.append(data)
    return jsonify({'message': 'Book added successfully'}), 201


@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books), 200


@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    genre = request.args.get('genre')
    results = books
    if author:
        results = [book for book in results if book['author'] == author]
    if published_year:
        results = [book for book in results if str(book['published_year']) == published_year]
    if genre:
        results = [book for book in results if book.get('genre') == genre]
    return jsonify(results), 200


@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    initial_length = len(books)
    books = [book for book in books if book['isbn'] != isbn]
    if len(books) < initial_length:
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404


@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    for book in books:
        if book['isbn'] == isbn:
            new_isbn = data.get('isbn')
            if new_isbn and new_isbn != isbn:
                # Check if the new ISBN already exists
                if any(b['isbn'] == new_isbn for b in books):
                    return jsonify({'message': f'Cannot update to ISBN {new_isbn} as it already exists'}), 400
            book.update(data)
            return jsonify({'message': 'Book updated successfully'}), 200
    return jsonify({'message': 'Book not found'}), 404


# Swagger UI configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'swagger_ui': 'swagger-ui-3.25.0',
        'app_name': "Library Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
