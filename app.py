from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def helloWorld():
    return 'Hello World. Fucking shit!'

@app.route('/<name>')
def helloName(name):
    return 'Hello {0}'.format(name) 

if __name__=='__main__':
    print(os.environ['APP_SETTINGS'])
    app.run(host='0.0.0.0', port=9000, debug=True)
    