
from flask import Flask, render_template
from flask import redirect, url_for, request      

app=Flask(__name__,template_folder='templates')

@app.route('/' , methods =['GET'])
def home():
    return render_template("BeeLaBoo Patterns Shop_bootstrap.html")
    
            
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:221022@localhost/beelaboo'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:221022@localhost/beelaboo'

app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

app = Flask(__name__)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(200), unique=True)
    pattern = db.Column(db.String(200), unique=True)
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def  __init__ (self, customer,  pattern,  rating , comments): 
        self.customer = customer
        self.pattern = pattern
        self.rating = rating
        self.comments = comments



@app.route('/feedback')

def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        pattern = request.form['pattern']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, pattern, rating, comments)
        if customer == '' or pattern == '':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, pattern, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, pattern, rating, comments)
            return render_template('success.html')

        return render_template('index.html', message='You have already submitted feedback')






    
if __name__ == "__main__":
    app.run(debug=True)
    
