import sqlite3, os
from flask import Flask, g, request, jsonify

app = Flask(__name__, template_folder='.')

@app.route('/login_form_vulnerable', methods=['POST','GET'])
def login_form_vulnerable():
    user_name = request.form['username']
    password = request.form['password']
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM employees WHERE username = '%s' AND password = '%s'" %(user_name, password))
    if cur.fetchone():
        result = {'status': 'success'}
    else:
        result = {'status': 'fail'}
    g.db.close()
    return jsonify(result)

def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.database = "./employees.db"
    if not os.path.exists(app.database):
        con = sqlite3.connect(app.database)
        cur = con.cursor()
        cur.execute('CREATE TABLE employees(username TEXT, password TEXT)')
        cur.execute('INSERT INTO employees VALUES("felix", "pwfelix")')
        con.commit()
        con.close()
        
    app.run()
    
    
# curl -d "username=felix&password=pwfelix" -X POST http://localhost:5000/login_form_vulnerable
# curl -d "username=felix&password=pwfeli" -X POST http://localhost:5000/login_form_vulnerable
# curl -d "username=felix&password=pwfeli" -X POST http://localhost:5000/login_form_vulnerable
# curl -d "username=felix&password=' OR 1 = 1;--" -X POST http://localhost:5000/login_form_vulnerable