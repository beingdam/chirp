from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f995a75ad60845f7b3fac2ae8c9504be'

database = [
    {
        'author': 'Soumya Dam',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date': 'Septempber 9, 2023',
    },
    {
        'author': 'Octo Boy',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date': 'Septempber 10, 2023',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', data=database)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)