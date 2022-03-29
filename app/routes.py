from app import myapp_obj
from flask import render_template, flash


@myapp_obj.route("/")

def home():
	name = {'name': 'Lisa'}
	city_names = ['Paris', 'London', 'Rome', 'Tahiti']
	return render_template('home.html',city_names = city_names, name=name)
