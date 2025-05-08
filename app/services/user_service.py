import os
import json
import bcrypt
from app.models.user import User
from app.utils.age_calculator import calculate_age
from datetime import datetime

class UserService:
    def __init__(self):
        os.makedirs('user_data', exist_ok=True)

    def register_user(self, form_data):
        if form_data['password'] != form_data['confirm_password']:
            raise ValueError("Passwords do not match")

        dob = datetime.strptime(form_data['dob'], '%Y-%m-%d')
        age = calculate_age(dob)

        password_hash = bcrypt.hashpw(form_data['password'].encode(), bcrypt.gensalt()).decode()

        user = User(
            firstname=form_data['firstname'],
            lastname=form_data['lastname'],
            dob=form_data['dob'],
            email=form_data['email'],
            mobile=form_data['mobile'],
            address=form_data['address'],
            age=age,
            password_hash=password_hash
        )

        filename = f"{user.firstname.lower()}_{user.lastname.lower()}.json"
        with open(os.path.join('user_data', filename), 'w') as f:
            json.dump(user.to_dict(), f, indent=4)
