import os

import firebase_admin
from firebase_admin import credentials, firestore

from flask import Flask
from flask_cors import CORS

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))

base = firebase_admin.initialize_app(cred)
db = firestore.client()

auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

app = Flask(__name__)
CORS(app)

from app import account_routes
from app import image_routes
from app import prompt_routes