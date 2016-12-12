import os

from flask import Flask
from flask import request
import numpy as np
import copy

app = Flask(__name__)


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@app.route('/simplewebapp')
def simple():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!!!'


@app.route('/simplewebapp/<int:copy_count>')
def copy_arr(copy_count):
    #f = open('./big.txt', 'r')
    #lines = f.readlines()
    #f.close()
    if copy_count <= 0:
        provider = str(os.environ.get('PROVIDER', 'world'))
        return 'Hello '+provider+'!!!!!'
    else:
        arr = np.zeros((1000, 1000))
        temp_arr = dict()
        for i in range(copy_count):
            temp_arr[i] = copy.copy(arr)

        return 'Hello numpy!!'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

