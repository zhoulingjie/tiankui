# coding: utf-8

from datetime import datetime
import pkgutil

from flask import Flask 
from flask import render_template

from .views.todos import todos_view
from .views.topics import tieba_view
from .views.tiantian import post_view


app = Flask(__name__)

# 动态路由
app.register_blueprint(todos_view, url_prefix='/todos')
app.register_blueprint(tieba_view, url_prefix='/tieba')
app.register_blueprint(post_view, url_prefix='/tian')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return str(datetime.now())


@app.route('/2048')
def game2048():
    return open('app/static/2048/index.html').read()

@app.route('/birth')
def xiaobao():
    return open('app/static/intresting/index.html').read()


@app.template_filter('format_date')
def format_date(date, format='%Y-%m-%d %H:%M'):
    return '{0:{1}}'.format(date, format)