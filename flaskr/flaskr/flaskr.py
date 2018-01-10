import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
	DATABASE=os.path.join(app.root_path,'flaskr.db'),
	SECRET_KEY='test1234',
	USERNAME='root',
	PASSWORD='test'))

app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(err):
	if hasattr(g,'sqlite_db'):
		g.sqlite_db.close()

def init_db():
	db = get_db()
	with app.open_resource('schema.sql',mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('Initialized Database')


@app.route('/')
def show_entries():
	db=get_db()
	cur=db.execute('SELECT `text`,title FROM entries ORDER BY id DESC')
	entries=cur.fetchall()
	return render_template('test.html',entries=entries)

@app.route('/reactive')
def reactive():
	data = 0;
	return render_template('reactive.html',data=data)

@app.route('/add', methods=['POST'])
def add_entry():

    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))