from datetime import datetime

from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from flask import Flask, render_template

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html',
		current_time=datetime.utcnow(), name='Wasif')

if __name__ == '__main__':    
	app.run(debug=True)
