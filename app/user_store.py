import json
import os

DATA_FILE = "/app/users.json"   # ← USE YOUR STRUCTURE

# Create file if missing
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)


def load_users():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def create_user(username, password, totp_secret):
    users = load_users()
    users[username] = {
        "password": password,
        "totp_secret": totp_secret
    }
    save_users(users)


def get_user(username):
    users = load_users()
    return users.get(username)
