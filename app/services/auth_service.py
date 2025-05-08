import os
import json
import bcrypt

class AuthService:
    def __init__(self):
        self.user_dir = 'user_data'

    def authenticate(self, email, password):
        for filename in os.listdir(self.user_dir):
            with open(os.path.join(self.user_dir, filename), 'r') as f:
                user_data = json.load(f)
                if user_data['email'] == email:
                    if bcrypt.checkpw(password.encode(), user_data['password_hash'].encode()):
                        return user_data
        return None
