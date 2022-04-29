# Import __init__ file
from __init__ import app
import sys
# JSON 
from bson import dumps
# login
@app.route('/', methods = ['GET'])
def login():
    try:
        # import users model
        from Model.models import Users,sqldb
        sqldb.init_app(app)
        sqldb.create_all()
        getUser = Users.query.all()
        print(getUser)
        return 'dsf'
    except Exception as e:
        print(e)
        return "error." 