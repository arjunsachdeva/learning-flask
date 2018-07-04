from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignupForm, LoginForm, NewProductRequestForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            newUser = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(newUser)
            db.session.commit()
            
            session['email'] = newUser.email
            return (url_for('home'))
        return "Success"
    elif request.method == 'GET':
        return render_template("signup.html", form=form)

@app.route("/home")
def home():
    #protect the pages
    if 'email' not in session:
        return redirect(url_for('login'))

    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("login.html", form=form)
        else:
            email = form.email.data
            password = form.password.data
           
            #Below line is querying the database. 
            user = User.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                session['email'] = form.email.data
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('login.html', form=form)

@app.route("/NewProductRequest", methods=['GET', 'POST'])
def new_product_request():
    form = NewProductRequestForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("NewProductRequest.html", form=form)
        else:
            session['email'] = form.email.data
            return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template("NewProductRequest.html", form=form)


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(debug=True)
