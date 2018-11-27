from nwtool import webapp, tools
from flask import render_template


@webapp.route('/')
@webapp.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@webapp.route('/pingtracker')
def pingtracker():
    txt = tools.group_ping()
    return render_template('pingtracker.html', title='Ping', txt=txt)
