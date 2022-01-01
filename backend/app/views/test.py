# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, flash, request, jsonify
from app.database import get_db

bp = Blueprint('test', __name__, url_prefix='/')

@bp.route('/test/', methods=('GET', 'POST'))
def test():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO notice (title, content) VALUES (?, ?)", (title, content)
            )
            db.commit()

        print('写数据库。标题：%s, 内容：%s' % (title, content))

    return render_template('test.html')

@bp.route('/test/wx', methods=('GET', 'POST'))
def test_wx_request():
    title = '测试'
    content = '测试公告内容'

    db = get_db()
    cur = db.execute(
        "SELECT title, content FROM notice ORDER BY id DESC"
    )

    data = cur.fetchall()
    print(data)
    title = data[0][0]
    content = data[0][1]
    print('请求数据库，返回数据。标题：%s, 内容：%s' % (title, content))
    return jsonify({'title': title, 'content': content})