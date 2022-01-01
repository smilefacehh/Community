# -*- coding:utf-8 -*-
from os import read
from flask import Blueprint, render_template, flash, request, jsonify
from app.database import get_db

bp = Blueprint('actions', __name__, url_prefix='/')

# 动作列表
@bp.route('/actions/', methods=['GET'])
def action_list():
    
    # 返回数据
    ret_data = {
        'bodyTypeMap': {},
        'instTypeMap': {},
        'actionTypeMap': {}
    }

    # 查action表
    db = get_db()
    data_action = db.execute(
        "SELECT * FROM action"
    )

    db_data_action = data_action.fetchall()

    actions = {}
    for row in db_data_action:
        action_id = row[0]
        action_name = row[1]
        body_type = row[2]
        body_name = row[3]
        inst_type = row[4]
        inst_name = row[5]
        content = row[6]
        img_url = row[7]

        if body_type not in ret_data['bodyTypeMap']:
            ret_data['bodyTypeMap'][body_type] = {'name': body_name}

        if inst_type not in ret_data['instTypeMap']:
            ret_data['instTypeMap'][inst_type] = {'name': inst_name}

        if action_id not in ret_data['actionTypeMap']:
            ret_data['actionTypeMap'][action_id] = {
                'name': action_name,
                'img': img_url,
                'content': content,
                'inst_type': inst_type,
                'body_type': body_type
            }

    return jsonify({'header': {'ret': 0}, 'content': ret_data})