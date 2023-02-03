# import the Flask & render template Library
from flask import Flask, render_template
# initialize the python flask
app = Flask(__name__)


@app.route('/')
def subindex():
    return render_template('subindex.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


#start the development server
if __name__ == '__main__':
    app.run(debug = True)
