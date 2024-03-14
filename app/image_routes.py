import json
import requests
import os

from app import app
from app import base
from app import auth_url

from flask import request, jsonify

from firebase_admin import auth

@app.route('/upload', methods=['POST'])
def upload():
    return "abc"