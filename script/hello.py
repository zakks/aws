import boto3, json, os

access_key=os.environ["ACCESS_KEY"]
secret_key=os.environ["SECRET_KEY"]

client = boto3.client('lambda', region_name='ap-south-1', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

## function to display hello world current time

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

## function to display login page

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/action_page')
def action():
    return render_template('action_page.html')

@app.route('/forgot_pass')
def forgot():
    return render_template('forgot_pass.html')

## function to display string in uppercase from lambda function

@app.route("/uc/<param>", methods=['GET'])
def helloworld(param):
    payload = '{"key":"%s"}' % (param)
    response = client.invoke(FunctionName='helloworld', Payload=payload)
    print(response)

    output= json.loads(response['Payload'].read().decode('utf-8'))
    result1 = {'input' :input ,'return_str':output}
    return render_template('upper.html', result=result1)


app.run(host='0.0.0.0', port=8888)

