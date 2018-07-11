from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

class ProductRequest(db.Model):
  __tablename__ = 'newproductrequest'
  uid = db.Column(db.Integer, primary_key = True)
  productname = db.Column(db.String(200))
  region = db.Column(db.String(200))
  technology = db.Column(db.String(200))
  userscategory = db.Column(db.String(200))
  environment = db.Column(db.String(200))
  servicecodetype = db.Column(db.String(200))
  dpiparameters = db.Column(db.String(200))
  policyname = db.Column(db.String(200))

  def __init__(self, productname, region, technology, userscategory, environment, servicecodetype, dpiparameters, policyname):
    self.productname = productname.title()
    self.region = region.title()
    self.technology = technology.title()
    self.userscategory = userscategory.title()
    self.environment = environment.title()
    self.servicecodetype = servicecodetype.title()
    self.dpiparameters = dpiparameters.title()
    self.policyname = policyname.title()


