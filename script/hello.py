from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

app.run(host='0.0.0.0', port=8888)
