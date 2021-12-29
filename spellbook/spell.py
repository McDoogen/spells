import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from spellbook.db import get_db

bp = Blueprint('spell', __name__, url_prefix='/spell')

@bp.route('/show', methods=['GET'])
def show():
    db = get_db()
    spell_scroll = db.execute('SELECT * FROM spells').fetchone()
    ingredient_list = spell_scroll['ingredients'].split(',')
    for i in range(len(ingredient_list)):
        ingredient_list[i] = f"{i+1}. {ingredient_list[i].strip()}"

    return render_template('spell/show.html', spell_scroll=spell_scroll, ingredient_list=ingredient_list)


@bp.before_app_request
def check():
    print("Run me first!")