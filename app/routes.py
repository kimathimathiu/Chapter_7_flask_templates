from app import app
from flask import render_template



@app.route('/login')
def login():
   """login URL"""
   return render_template ('login.html', title="Login")


@app.route('/register')
def register():
   """Register URL"""
   return render_template ('register.html', title="Register")


@app.route('/')
@app.route('/shop')
def shop():
   """ URL"""
   return render_template ('shop.html', title="Shop")