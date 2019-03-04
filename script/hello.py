import boto3, json
client = boto3.client('lambda', region_name='ap-south-1', aws_access_key_id='AKIAI3ZYDANHF7TA6AYA', aws_secret_access_key='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')

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/uc/<input>", methods=['GET'])
def change_uppercase(input):
    ##input = "sourav"
    payload = '{"key":"%s"}' % (input)
    response = client.invoke(FunctionName='helloworld', Payload=payload)
    print(response)

    output= json.loads(response['Payload'].read().decode('utf-8'))
    result1 = {'input' :input ,'return_str':output}
    return render_template('lowertouppercase.html', result=result1)

@app.route('/login')
def login():
    return render_template('login.html')


app.run(host='0.0.0.0', port=8888)
