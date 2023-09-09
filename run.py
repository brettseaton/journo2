import os
import glob
from flask import Flask, render_template, jsonify, request
from flask import request
from prompt import inference
from flask_sse import sse
from emailDownload import summarize_with_openai, concatenate_summaries, main
from celery_config import celery

app = Flask(__name__)

@app.route('/generation', methods=['GET'])
def generation_tool():
    return render_template('generation.html')

app.register_blueprint(sse, url_prefix='/stream')

@app.route('/crime_summaries', methods=['GET'])
def crime_summaries():
    tasks = main()
    task_ids = tasks.get('task_ids', [])
    all_summaries = tasks.get('all_summaries', {})
    return render_template('crime_summaries.html', task_ids=task_ids)

@app.route('/status/<task_ids>', methods=['GET'])
def taskstatus(task_ids):
    task_ids_list = task_ids.split(',')
    task_states = {}
    
    for task_id in task_ids_list:
        task = celery.AsyncResult(task_id)
        state_info = {'state': task.state, 'status': 'Pending...' if task.state == 'PENDING' else 'Task completed'}
        sse.publish({"message": state_info}, type='greeting')
        task_states[task_id] = state_info
    
    return jsonify(task_states)


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