# -*- coding:utf-8 -*-
from flask import Flask
from .config import config

app = Flask(__name__)
app.config.from_object(config['development'])

# 数据库
from . import database
database.init_app(app)

# 视图
from app.views import train
app.register_blueprint(train.bp)
from app.views import actions
app.register_blueprint(actions.bp)