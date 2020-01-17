from flask import request, render_template, flash, url_for, redirect

def home():
    return render_template('index.html')

def login():
    return render_template('login.html')