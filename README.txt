README

QUICK START FOR LOCAL:
1. open XAMPP
2. start Apache and MySQL
3. go to https://localhost (port is 3306)
4. press phpMyAdmin at the top right
5. see the database on the left named "flask" with table name "user_info"
6. open cmd
7. cd builds
8. cd flask-login-system
9. run python main.py
10. go to the link and type /form and fill out the form and it will be sent to the MySQL database


Description:
Simple login system with Flask, MySQL
Userrname rules: 6-20 characters, must not be in db already
Password rules: 6-20 characters, must match confirm-password
Password encryption by Werkzeug which is a python library which returns the hashed version of the password


Portfolio Pictures: 800x650
Itch.io Game Pictures: 630x500

Possible Addition: Gifs instead of portfolio pictures?
