import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('chart', __name__)

@bp.route('/')
def chart():
    db = get_db()
    posts = db.execute(
        'SELECT username, COUNT(username)'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' GROUP BY username'
        ' ORDER BY username DESC'
    ).fetchall()
    return render_template('chart/chart.html', posts=posts)
