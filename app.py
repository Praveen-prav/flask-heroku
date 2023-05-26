from flask import Flask, jsonify, request, url_for
import ssl

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    server_url = request.base_url
    books = [
        {
            'name': "There's a Monster",
            'author': 'Danielle Bruckert',
            'description': 'Description 1',
            'language': 'English',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book1.png'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book1.pdf'),
            'genre' : 'Fiction'
        },
        {
            'name': 'The fox who wanted to fly.',
            'author': 'M.Fox',
            'description': 'Description 2',
            'language': 'Hindi',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book2.png'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book2.pdf'),
            'genre' : 'Non Fiction'
        },
        {
            'name': 'Under My Pillow',
            'author': 'Jennifer Ballow',
            'description': 'Description 3',
            'language': 'Telugu',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book3.png'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book3.pdf'),
            'genre' : 'Fiction'
        },
        {
            'name': 'Welcome to Creply Hollow',
            'author': 'Aurora S. Forst',
            'description': 'Description 4',
            'language': 'Tamil',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book4.png'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book4.pdf'),
            'genre' : 'Non Fiction'
        },
        {
            'name': 'The Golden Flower',
            'author': 'Lee Gamboa',
            'description': 'Description 5',
            'language': 'English',
            'cover_image_path': server_url + url_for('static', filename='assets/images/book5.png'),
            'pdf_path': server_url + url_for('static', filename='assets/pdfs/book5.pdf'),
            'genre' : 'Fiction'
        }
    ]
    return jsonify(books)

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host="0.0.0.0", port=51000, debug=True, ssl_context=context)
