from flask import Blueprint, request, render_template, redirect, session, url_for
from app.services.auth_service import AuthService

login_bp = Blueprint('login', __name__)
auth_service = AuthService()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = auth_service.authenticate(request.form['email'], request.form['password'])
        if user:
            session['user'] = {'firstname': user['firstname'], 'lastname': user['lastname']}
            return redirect(url_for('home.index'))
        return "Invalid credentials", 401
    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home.index'))
