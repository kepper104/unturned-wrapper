import random
import re
import sys
from flask import Flask, render_template
from turbo_flask import Turbo
import threading
from time import sleep
app = Flask(__name__)
turbo = Turbo(app)
@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/page2')
def page2():
    return render_template('index3.html')

@app.context_processor
def inject_load():
    print(sys.platform)
    if sys.platform.startswith('linux'): 
        with open('/proc/loadavg', 'rt') as f:
            load = f.read().split()[0:3]
    else:
        load = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'load1': load[0], 'load5': load[1], 'load15': load[2]}

def update_load():
    with app.app_context():
        while True:
            sleep(0.1)
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))
@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

app.run(debug=False, host='0.0.0.0')