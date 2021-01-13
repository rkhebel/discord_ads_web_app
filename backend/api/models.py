from . import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(db.Model):
  """User account model."""

  __tablename__ = 'users'

  # COLUMNS
  
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  first_name = db.Column(
    db.String(100),
    nullable=False,
    unique=False
  )
  last_name = db.Column(
    db.String(100),
    nullable=False,
    unique=False
  )
  email = db.Column(
    db.String(40),
    unique=False,
    nullable=False
  )
  password = db.Column(
    db.String(200),
    primary_key=False,
    unique=False,
    nullable=False
  )
  user_type = db.Column(
    db.String(60),
    index=False,
    unique=False,
    nullable=False
  )
  created_on = db.Column(
    db.DateTime,
    default=datetime.datetime.now()
  )
  updated_at = db.Column(
    db.DateTime,
    onupdate = datetime.datetime.now()
  )

  # RELATIONSHIPS
  advertisements = db.relationship('Advertisement', backref='user', cascade = 'all, delete') #deletes all ads when account is deleted

  # METHODS
  def set_password(self, password):
      """Create hashed password."""
      self.password = generate_password_hash(
          password,
          method='sha256'
      )

  def check_password(self, password):
      """Check hashed password."""
      return check_password_hash(self.password, password)

  def __repr__(self):
      return '<User {}>'.format(self.username)


#model for advertisements
class Advertisement(db.Model):

  __tablename__ = 'advertisements'

  # COLUMNS
  id = db.Column(
    db.Integer,
    primary_key=True
  )
  user_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
  )
  name = db.Column(
    db.String(200),
    nullable = False,
    unique = False
  )
  description = db.Column(
    db.String(1024),
    nullable = False,
    unique = False
  )
  content = db.Column(
    db.String(1024),
    nullable = False,
    unique = False
  )
  created_on = db.Column(
    db.DateTime,
    default=datetime.datetime.now()
  )
  updated_at = db.Column(
    db.DateTime,
    onupdate = datetime.datetime.now()
  )

  # METHODS
  def __repr__(self):
    return '<Advertisement {}>'.format(self.name)

