from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
)
from forms import LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
app = Flask(__name__)


app.config['SECRET_KEY'] = '84599-9177826cc333?9aba10edd9F6fdf39c6fe194717b431bf2deXt0fa5286b4e75'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utenti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_PERMANENT"] = False
db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            return render_template("login.html", form = form, message = "Wrong Credentials, Please Try Again")
        else:
            session['user'] = user.email
            return redirect(url_for('profile'))
    return render_template("login.html", form = form)

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
        ''' remember to change to https for a secure connection '''
    return redirect(url_for("index", _scheme='http', _external=True))

@app.route('/profile')
def profile():
    if not session.get('user'):
        return redirect(url_for('login'))

    return render_template('profile.html')

