import os
from flask import Flask, render_template
from flask import request
from prompt import inference
from emailDownload import main
from celery import Celery

app = Flask(__name__)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['result_backend'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6380/0',
    result_backend='redis://localhost:6380/0'
)

celery = make_celery(app)

@app.route('/generation', methods=['GET'])
def generation_tool():
    return render_template('generation.html')

@app.route('/crime_summaries', methods=['GET'])
def crime_summaries():
    summaries = main()
    return render_template('crime_summaries.html', summaries=summaries)

@app.route('/', methods=['GET', 'POST'])
def index():
	result = ""
	if request.method == "POST":
		print("POST")
		#print(request.form["dropdown"], request.form["content"])

		#result = inference(request.form["dropdown"], request.form["content"])
		result = inference(request.form["dropdown"], request.form["content"])
	else:
		print("GET")
	return render_template('index.html', result = result)

# Keep this at the bottom of app.py

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)