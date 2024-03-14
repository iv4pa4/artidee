import json
import requests
import os

from app import app
from app import base
from app import db
from app import auth_url

from flask import request, jsonify

from firebase_admin import auth

@app.route('/upload', methods=['POST'])
def upload():
    json_data = request.json
    uid = json_data['uid']
    filename = json_data['filename']
