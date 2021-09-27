from flask import Flask, flash, render_template, session, redirect, url_for
import sys
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email 


class NameForm(FlaskForm):    
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sda'
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():  
	name = None    
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', 
				form=form, 
				name=name)


if __name__ == '__main__':    
	app.run(debug=True)
