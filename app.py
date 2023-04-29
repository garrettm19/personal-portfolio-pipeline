from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Mgarrett620:carsonJ32!@personalportfoliodb.c4eus8splhyx.us-east-1.rds.amazonaws.com/personalportfoliodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'bj\x18\x07\xf9_\xaf\x1c\xfb6\xc6\x8cfq!\xf7\xb6\xee>i\xcf\xf2\x03\x10G'

db = SQLAlchemy(app)

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))

@app.route('/', methods=['GET'])
def index():
    logged_in = session.get('logged_in', False)
    return render_template('index.html', logged_in=logged_in)

@app.route('/login', methods=['GET', 'POST'])
def signin():
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username exists in the database
        user = UserInfo.query.filter_by(username=username).first()
        if user is None:
            error_message = "Username not found."
        else:
            # Check if the password is correct
            hashed_password = user.password
            if not check_password_hash(hashed_password, password):
                error_message = "Incorrect password."
            else:
                session['logged_in'] = True
                session['username'] = username
                return redirect(url_for('index'))
    
    return render_template('login.html', error_message=error_message)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = ""
    if request.method == 'POST':
        if 'username' not in request.form:
            error_message = "Username not found."
        else:
            username = request.form['username']
        
        if 'password' not in request.form:
            error_message = "Password not found."
        else:
            password = request.form['password']
        
        if 'confirm_password' not in request.form:
            error_message = "Confirm password not found."
        else:
            confirm_password = request.form['confirm_password']
        
        if len(username) < 6 or len(username) > 20 or ' ' in username:
            error_message = "Username must be between 6 and 20 characters and cannot contain spaces."
        elif len(password) < 6 or len(password) > 20 or ' ' in password:
            error_message = "Password must be between 6 and 20 characters and cannot contain spaces."
        elif password != confirm_password:
            error_message = "Passwords do not match."
        else:
            hashed_password = generate_password_hash(password)
            
            # Check if the username already exists in the database
            user = UserInfo.query.filter_by(username=username).first()
            if user is not None:
                error_message = "Username already exists."
            else:
                # Insert the new user into the database
                new_user = UserInfo(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                
                return render_template('login.html', error_message=f"Thanks for signing up, {username}!")
    
    return render_template('login.html', error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)