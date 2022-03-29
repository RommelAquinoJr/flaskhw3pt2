from app import myobj
from flask import render_template, flash

@myobj.route("/")

def home():
	return render_template('home.html',city_names = city_names, name=name)
name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']
