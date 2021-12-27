import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from spellbook.db import get_db

bp = Blueprint('spell', __name__, url_prefix='/spell')

@bp.route('/show', methods=['GET'])
def show():
    return render_template('spell/show.html')

@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        pass
    
    return render_template('spell/edit.html')

@bp.before_app_request
def check():
    print("Run me first!")