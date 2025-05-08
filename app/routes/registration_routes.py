from flask import Blueprint, request, render_template, redirect, url_for
from app.services.user_service import UserService

registration_bp = Blueprint('register', __name__)
user_service = UserService()

@registration_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user_service.register_user(request.form)
            return redirect(url_for('login.login'))
        except ValueError as e:
            return str(e), 400
    return render_template('register.html')
