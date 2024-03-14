import os

import firebase_admin
from firebase_admin import credentials

from flask import Flask

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))

base = firebase_admin.initialize_app(cred)

auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

app = Flask(__name__)

from app import views