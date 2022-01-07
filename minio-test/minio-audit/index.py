from flask import Flask, jsonify, request , render_template, redirect, url_for, json, flash, session
from pathlib import Path
import os
from flask_login import logout_user

audit = open("minio_audit.json", "a")
server = open("minio_server.json" , "a")

os.chown("minio_audit.json", 1000, 1000 )
os.chown("minio_server.json", 1000, 1000 )

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

minio_audit = [
  { 'application': 'flask', 'status': 'running' }
]

minio_server = [
  { 'application': 'flask', 'status': 'running' }
]

@app.route('/')
def home():
  return render_template("index.html")


@app.route('/minio_audit_logs')
def minio_get():
  return jsonify(open("minio_audit.json", "r").read())

@app.route('/minio_server_logs')
def minio_server_get():
  return jsonify(open("minio_server.json", "r").read())

@app.route('/minio_audit_logs', methods=['POST'])
def minio_post():
  minio_audit.append(request.get_json())
  audit.write(json.dumps(request.get_json(), indent=4))
  return '', 204

@app.route('/minio_server_logs', methods=['POST'])
def minio_server_post():
  minio_server.append(request.get_json())
  server.write(json.dumps(request.get_json(), indent=4))
  return '', 204

@app.route('/login', methods=['GET', 'POST'])
def login():
# import the Flask class from the flask module
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'minio':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('minio.html')
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
   # session.pop('username', None)
   # return render_template("index.html")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
