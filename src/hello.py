from datetime import datetime
from flask import Flask, flash, render_template, session, redirect, url_for
import sys
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
UOFT_EMAIL_INDICATOR = 'utoronto'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?',
                       validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sda'
moment = Moment(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        print('old name:', file=sys.stderr)
        print(old_name, file=sys.stderr)
        print('new name:', file=sys.stderr)
        print(form.name.data, file=sys.stderr)
        print('old email:', file=sys.stderr)
        print(old_email, file=sys.stderr)
        print('new email:', file=sys.stderr)
        print(form.email.data, file=sys.stderr)
        if old_name is not None and old_name != form.name.data:
            print('New name detected, should show flash!', file=sys.stderr)
            flash('Looks like you have changed your name!')
        if old_email is not None and old_name != form.name.data:
            print('New email detected, should show flash!', file=sys.stderr)
            flash('Looks like you have changed your email!')

        session['name'] = form.name.data
        session['email'] = form.email.data
        session['is_uoft_email'] = UOFT_EMAIL_INDICATOR in session['email']
        return redirect(url_for('index'))

    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           email=session.get('email'),
                           is_uoft_email=session.get('is_uoft_email'))


# just to clear session
@app.route('/delete-session/')
def delete_visits():
    session.pop('name', None)  # delete visits
    session.pop('email', None)
    session.pop('is_uoft_email', None)
    return 'Visits deleted'


if __name__ == '__main__':
    app.run(debug=True)
