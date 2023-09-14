from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@chirp.in' and form.password.data == 'password':
            flash('You have been loged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Email or password invalid!', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)