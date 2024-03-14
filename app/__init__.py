import firebase_admin
from firebase_admin import credentials

from flask import Flask

cred = credentials.Certificate("kocosi-firebase-key.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

from app import views