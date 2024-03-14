import os

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials

from flask import Flask

cred = credentials.Certificate(os.path.join(os.getcwd(), "app\\kocosi-firebase-key.json"))

base = firebase_admin.initialize_app(cred)

auth_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

app = Flask(__name__)

db = firestore.Client()

from app import account_routes
from app import image_routes