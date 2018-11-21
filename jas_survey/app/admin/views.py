from . import admin
from flask import render_template
import sqlite3 as sql


@admin.route('/login')
def login():
    return render_template('admin/login.html')


@admin.route('/list')
def list():
    activeTab = '1'
    con = sql.connect("dev-database.sqlite")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from SURVEYS")

    rows = cur.fetchall()

    return render_template('admin/list.html', rows=rows, activeTab=activeTab)
