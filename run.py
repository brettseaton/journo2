from flask import Flask, render_template
from flask import request
from prompt import inference

app = Flask(__name__)

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

app.run(port=8080, debug=True)