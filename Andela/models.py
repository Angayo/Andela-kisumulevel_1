from run import db
from passlib.hash import pbkdf2_sha256 as sha256

class Register(db.Model):
    '''
         Register class
    '''
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    sur_name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(80), unique=True)

def __init__(self, data):
    self.first_name = data.get('first_name')
    self.last_name = data.get('last_name')
    self.sur_name =data.get('sur_name')
    self.email =data.get('email')
    self.username =data.get('username')


def fullname(self):
    return '{}{}{}{}'.format(self.first_name, self.last_name, self.sur_name, self.username)

def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.create_all()
    
@classmethod
def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

@classmethod
def delete_all(cls):
    try:
        num_rows_deleted = db.session.query(cls).delete()
        db.session.commit()
        return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
    except:
        return {'message': 'Something went wrong'}

@staticmethod
def generate_hash(password):
    return sha256.hash(password)
    
@staticmethod
def verify_hash(password, hash):
        return sha256.verify(password, hash)

@staticmethod
def get_users():
    return Register.query.get(id)

def __repr__(self):
    return'<id {}>'.format(self.id)


class Comment(db.Model):

  __tablename__ = 'Post_comment'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  contents = db.Column(db.Text, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.title = data.get('title')
    self.contents = data.get('contents')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
@staticmethod
def get_all_comment():
    return comments.query.all()
  
@staticmethod
def get_one_comment(id):
    return commentModel.query.get(id)

def __repr__(self):
    return '<id {}>'.format(self.id)

class Token_revokeModel(db.Model):
    __tablename__ = 'token_revoke'
    
    id = db.Column(db.Integer, primary_key = True)
    jt = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
@classmethod
def jt_blacklisted(cls, jt):
    query = cls.query.filter_by(jt = jt).first()
    return bool(query)
