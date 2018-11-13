from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome.....  to '
@app.route('/home')
def home():
    return 'home page'

@app.route('/about')
def about():
    return "About Page"
if (__name__ == '__main__'):
   app.run(debug=True)