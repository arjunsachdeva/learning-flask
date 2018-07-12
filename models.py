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
  __tablename__ = 'datanewproductrequest'
  uid = db.Column(db.Integer, primary_key = True)
  productname = db.Column(db.String(200))
  region = db.Column(db.String(200))
  technology = db.Column(db.String(200))
  userscategory = db.Column(db.String(200))
  environment = db.Column(db.String(200))
  servicecodetype = db.Column(db.String(200))
  dpi_fl_rate_limit = db.Column(db.String(200))
  dpi_rl_rate_limit = db.Column(db.String(200))
  dpi_fl_volume_control = db.Column(db.String(200))
  dpi_rl_volume_control = db.Column(db.String(200))
  dpi_fl_rate_limit_post = db.Column(db.String(200))
  dpi_rl_rate_limit_post = db.Column(db.String(200))
  dpi_fl_voip_rate_limit = db.Column(db.String(200))
  dpi_rl_voip_rate_limit = db.Column(db.String(200))
  dpi_blocking_feature = db.Column(db.String(200))
  dpi_shaping_feature = db.Column(db.String(200))
  dpi_allow_feature = db.Column(db.String(200))
  dpi_content_filter = db.Column(db.String(200))
  dpi_msg_whitelist = db.Column(db.String(200))
  dpi_big_sockets = db.Column(db.String(200))
  dpi_acpu_release = db.Column(db.String(200))
  policyname = db.Column(db.String(200))

  def __init__(self, form):
    self.productname = form.productName.data.title()
    self.region = form.region.data.title()
    self.technology = form.technology.data.title()
    self.userscategory = form.usersCategory.data.title()
    self.environment = form.environment.data.title()
    self.servicecodetype = form.serviceCodeType.data.title()


    self.dpi_fl_rate_limit      = form.dpi_fl_rate_limit.data.title()
    self.dpi_rl_rate_limit      = form.dpi_rl_rate_limit.data.title()
    self.dpi_fl_volume_control  = form.dpi_fl_volume_control.data.title()
    self.dpi_rl_volume_control  = form.dpi_rl_volume_control.data.title()
    self.dpi_fl_rate_limit_post = form.dpi_fl_rate_limit_post.data.title()
    self.dpi_rl_rate_limit_post = form.dpi_rl_rate_limit_post.data.title()
    self.dpi_fl_voip_rate_limit = form.dpi_fl_voip_rate_limit.data.title()
    self.dpi_rl_voip_rate_limit = form.dpi_rl_voip_rate_limit.data.title()
    self.dpi_blocking_feature   = form.dpi_blocking_feature.data.title()
    self.dpi_shaping_feature    = form.dpi_shaping_feature.data.title()
    self.dpi_allow_feature      = form.dpi_allow_feature.data.title()
    self.dpi_content_filter     = form.dpi_content_filter.data.title()
    self.dpi_msg_whitelist      = form.dpi_msg_whitelist.data.title()
    self.dpi_big_sockets        = form.dpi_big_sockets.data.title()
    self.dpi_acpu_release       = form.dpi_acpu_release.data.title()


    self.policyname = form.policyName.data.title()


