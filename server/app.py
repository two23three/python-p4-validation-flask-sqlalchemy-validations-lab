from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

@app.route('/api/authors')
def get_authors():
    authors = Author.query.all()
    response = [author.to_dict() for author in authors]
    return make_response(response, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)