from flask import Flask, render_template
from flask import request
from prompt import complete_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	result = ""
	if request.method == "POST":
		print("POST")
		url = request.form['url']
		result = complete_sentence(url)

	return render_template('index.html', result = result)

# Keep this at the bottom of app.py
app.run(debug=True)