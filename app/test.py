# from flask import Flask
# from flask_wtf import Form
# from wtforms import StringField
# from flask import render_template
# app = Flask(__name__)
#
# class u(Form):
#     username = StringField('userName')
#
#
# @app.route('/')
# def home():
#     #f = u()
#     return render_template('account/signup.html', form=u())
#
# app.config.from_pyfile('_settings.py')
#
# app.debug=True
#
# app.run()