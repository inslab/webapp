import os

from flask import Flask
from flask import request
import importlib

app = Flask(__name__)


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@app.route('/simplewebapp')
def simple():
    #f = open('./big.txt', 'r')
    #lines = f.readlines()
    #f.close()
    module = request.args.get('module')
    if module == 'numpy':
        importlib.import_module(module)
        return 'Hello numpy!!'
    else:
        provider = str(os.environ.get('PROVIDER', 'world'))
        return 'Hello '+provider+'!!!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
