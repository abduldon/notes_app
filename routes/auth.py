from flask import  {
Blueprint,
    render_templates,
    request,
    redirect,
    url_for,
    flash
}
from extensions import db
from models import User
from werkzeug.security import(
    generate_password_hash,
     check_password_hash
)

auth_bp=Blueprint('auth',__name__)

@auth_bp.route('/')
def home ():
    return render_templates('index.html')

@auth_bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username