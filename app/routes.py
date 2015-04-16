import os, json, logging
from flask import request, redirect, url_for, render_template, jsonify, Response
from app import app


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
