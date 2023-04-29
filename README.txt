flaskhelp

flask run = python -m flask run

http://localhost:5000/hello (because there is a @route.hello)
make sure when u run the server u add /hello to the end of the localhost link

QUICK START:
1. open XAMPP
2. start Apache and MySQL
3. go to https://localhost (port is 3306)
4. press phpMyAdmin at the top right
5. see the database on the left named "flask" with table name "info_table"
made new database with name "user_info"

6. open cmd
7. cd builds
8. cd flask-login-system
9. run python main.py
10. go to the link and type /form and fill out the form and it will be sent to the MySQL database

use chatgpt to make pages

next steps:
1. Add login system to portfolio website
2. formatting it will be the hardest part, use perplexity AI and write put the login system in the top left.

completed:
hashing password / sign up sheet is working




Description:
Simple login system with Flask, MySQL
Userrname rules: 6-20 characters, must not be in db already
Password rules: 6-20 characters, must match confirm-password
Password encryption by Werkzeug which is a python library which returns the hashed version of the password


-Update error message to go to main index file and display successfully logged in for user.
-Add one more page to this so it hits three pages

upload all unity games on the website and all projects,
upload gifs for all the screenshots

800x650 my work ss
630x500 itchio ss


Can you write me a simple python code that will sign up the user if the username has a length between 6 and 20 characters, spaces are not allowed, also the password has a length between 6 and 20 characters, spaces are not allowed. The input form has a variable for the username, the password and confirmation of the password. I need to check if the passwords match and that the username is unique. Make it similar to this code:
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO users (name, password) VALUES(%s, %s)''', (name, hashed_password))
        mysql.connection.commit()
        cursor.close()
        return f"Thanks for signing up, {name}!"
    return render_template('signup.html', form=form)