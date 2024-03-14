import os

import firebase_admin
from firebase_admin import credentials, firestore

from flask import Flask

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))

base = firebase_admin.initialize_app(cred)
db = firestore.client()

auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

app = Flask(__name__)

db = firestore.client()

from app import account_routes
from app import image_routes