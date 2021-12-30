import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from spellbook_api.db import get_db

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    db = get_db()
    spell_cursor = db.execute('SELECT * FROM spells').fetchone()
    ingredient_list = spell_cursor['ingredients'].split(',')
    spell_name = spell_cursor['spell_name']
    spell_author = spell_cursor['author']
    for i in range(len(ingredient_list)):
        ingredient_list[i] = f"{i+1}. {ingredient_list[i].strip()}"
    
    spell_cursor = db.execute('SELECT spell_name FROM spells')
    spell_list = []
    for item in spell_cursor:
        spell_list.append(item['spell_name'])

    return render_template(
        'index/index.html',
        spell_name=spell_name,
        spell_author=spell_author,
        ingredient_list=ingredient_list,
        spell_list=spell_list
    )