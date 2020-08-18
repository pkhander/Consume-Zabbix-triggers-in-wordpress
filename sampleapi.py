""" Same API for wordpress plugin to consume"""

from flask import Flask, jsonify
from triggers import get_triggers
app = Flask(__name__)


@app.route('/triggers')
def trigger():
    response = get_triggers()
    return response


if __name__ == '__main__':
    app.run(host ='0.0.0.0' , port = '80',debug=True)

