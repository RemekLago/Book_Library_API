from book_library_app import app
from flask import jsonify

import book_library_app
from book_library_app.models import Author, AuthorsSchema, author_schema


@app.route('/')
def index():
    return 'WORKS'


@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    authors_schema = AuthorsSchema(many=True)
    return jsonify({
        'sucess': True,
        'data': authors_schema.dump(authors),
        'number_of_records': len(authors)
    })
    
@app.route('/api/v1/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get_or_404(author_id, description=f'Author with id {author_id} not found')
    return jsonify({
        'sucess': True,
        'data': author_schema.dump(author)
    })
    
@app.route('/api/v1/authors', methods=['POST'])
def create_author():
    return jsonify({
        'sucess': True,
        'data': 'New author has been created'
    }), 201
    
@app.route('/api/v1/authors/<author_id>', methods=['PUT'])
def update_author(author_id):
    return jsonify({
        'sucess': True,
        'data': f'Author with {author_id} has been updated '
    })

@app.route('/api/v1/authors/<author_id>', methods=['DELETE'])
def delete_author(author_id):
    return jsonify({
        'sucess': True,
        'data': f'Author with {author_id} has been deleted '
    })
    
