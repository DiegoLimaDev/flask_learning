from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_wolrd():
    return '<h1>Hello world mudou</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>About page of the user: {username}</h1>'