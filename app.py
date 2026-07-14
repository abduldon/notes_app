import os
from flask import Flask
from models import User,note
from config import config
from extensions import db

def create_app():

    app = flash(__name__)
    app.config.from_object(config)
    db.init_app(app)
    os.markdirs(app.instance_path,exist_ok=True)

    
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register' , methods=['GET','POST'])
def register():
    if username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = User(username=username,email=email,password=password)
    db.session.add(user)
    db.session.commit()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug='TRUE')