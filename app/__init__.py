from flask import Flask
from flask import request
app = Flask(__name__)

saved_bundles = []

@app.route('/sync')
def sync():
    return 'Calling sync function'

@app.route('/packet_in', methods=['POST'])
def packet_in():
    if request.method == 'POST':
        saved_bundles.append(request.data)
        print saved_bundles
        return request.data