from datetime import datetime
from typing_extensions import Annotated
from flask import Flask, render_template, url_for, flash, redirect, session
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


from forms import RegistrationForm, LoginForm

# timestamp = Annotated[
#     datetime.datetime,
#     mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
# ]

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f995a75ad60845f7b3fac2ae8c9504be'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    image_file: Mapped[str] = mapped_column(String(120), nullable=False, default='default.jpg')
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)
    posts: Mapped["Post"] = relationship(backref="author", lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    # date_posted: Mapped[timestamp] = mapped_column(server_default=func.UTC_TIMESTAMP())
    date_posted: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[str] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    
with app.app_context():
    db.create_all()

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
        if form.email.data == 'admin@chirp.in' and form.password.data == 'chirp':
            flash('You have been loged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Email or password invalid!', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)