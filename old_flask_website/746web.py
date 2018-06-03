import os
import re
import shutil
import sqlite3
from flask import Flask, render_template, request, abort, send_file
from tempfile import NamedTemporaryFile
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('homepage.html')