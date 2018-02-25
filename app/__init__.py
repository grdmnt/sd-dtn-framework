from flask import Flask
from flask import request
app = Flask(__name__)

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

cache.set('saved_bundles', [])

@app.route('/sync')
def sync():
    return 'Calling sync function'

@app.route('/packet_in', methods=['POST'])
def packet_in():
    if request.method == 'POST':
        saved_bundles = cache.get('saved_bundles')
        saved_bundles.append(request.data)
        cache.set('saved_bundles', saved_bundles)
        return str(saved_bundles)