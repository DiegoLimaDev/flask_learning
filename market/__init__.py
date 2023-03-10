# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# db = SQLAlchemy()
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
# db.init_app(app)

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
#     db.init_app(app)
#     return app

# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False, unique=True)
#     price = db.Column(db.Integer, nullable=False)
#     barcode = db.Column(db.String(12), nullable=False, unique=True)
#     description = db.Column(db.String(1024), nullable=False, unique=True)

#     def __repr__(self):
#         return f'Item {self.name}'

# @app.route('/')
# @app.route('/home')
# def home_page():
#     return render_template('home.html')

# @app.route('/market')
# def market_page():
#     items = Item.query.all()
#     return render_template('market.html', items=items)


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///market.db'
    db.init_app(app)
    return app
