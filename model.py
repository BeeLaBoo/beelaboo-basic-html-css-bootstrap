from ..database import create_app
sqldb = create_app()
#  Users Model
class Users(sqldb.Model):
    __tablename__ = 'users'
    id = sqldb.Column(sqldb.Integer, primary_key = True)
    db = sqldb.Column(sqldb.String(40))
    def __init__(self,email,db):
        self.email = email
        self.db = db
    def __repr__(self,db):
        return '<USER %r>' % self.db