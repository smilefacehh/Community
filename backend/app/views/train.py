# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, flash, request, jsonify
from app.database import get_db
import time
import datetime
import json

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
today_start_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d')))
today_end_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1

bp = Blueprint('train', __name__, url_prefix='/')


# 今日训练动作数据
@bp.route('/train/actions/', methods=['GET', 'POST'])
def action_list():
    """
    ret_data:{
        2: { -- 动作id
            1: { -- 组
                unit: 0,
                weight: 20,
                num: 12
            }
        }
    }
    """
    if request.method == 'GET':
        user_id = request.args.get('userid')

        if not user_id:
            return jsonify({'header': {'ret': 101}})

        # 返回数据
        ret_data = {}

        # 查train表
        db = get_db()
        cur_train = db.execute(
            "SELECT * FROM train WHERE user_id=%s and created>=%d and created<=%d" % (user_id, today_start_time, today_end_time)
        )

        db_data_train = cur_train.fetchall()

        for row in db_data_train:
            action_id = row[2]
            group_idx = row[3]
            weight = row[4]
            group_num = row[5]
            weight_unit = row[6]

            if action_id not in ret_data:
                ret_data[action_id] = {}
            if group_idx not in ret_data[action_id]:
                ret_data[action_id][group_idx] = {}

            ret_data[action_id][group_idx]['unit'] = weight_unit
            ret_data[action_id][group_idx]['weight'] = weight
            ret_data[action_id][group_idx]['num'] = group_num

        return jsonify({'header': {'ret': 0}, 'content': ret_data})
    
    if request.method == 'POST':
        data = json.loads(request.data)
        user_id = int(data['userid'])
        records = data['records']
        
        if not user_id:
            return jsonify({'header': {'ret': 102}})

        db = get_db()
        db.execute(
            "DELETE FROM train WHERE user_id=%d and created>=%d and created<=%d and action_id=%d" % (user_id, today_start_time, today_end_time, int(records['action_id']))
        )

        print(records)
        
        for i in range(len(records['record_list'])):
            group_idx = i + 1
            unit = int(records['record_list'][i]['unit'])
            weight = int(records['record_list'][i]['weight'])
            num = int(records['record_list'][i]['num'])
            db.execute(
                'INSERT INTO train (user_id, created, action_id, group_idx, weight, group_num, weight_unit) '
                'VALUES (%d,%d,%d,%d,%d,%d,%d)' % (user_id, int(time.time()), int(records['action_id']), group_idx, weight, num, unit)
            )
        db.commit()

        return jsonify({'header': {'ret': 0}})
        
    return jsonify({'header': {'ret': -1}})