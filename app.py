from flask import Flask, url_for, abort, redirect, current_app, render_template, request, session
from flask_session import Session
from redis import Redis
import re, os, ConfigParser
inifile = ConfigParser.SafeConfigParser()


STAGE = os.environ.get('ENV_STAGE', 'dev')
inifile.read(os.path.join(os.path.dirname(__file__), 'config/%s.ini' % STAGE))

app = Flask(__name__)

app.url_map.strict_slashes = False
redis = Redis(host=inifile.get('redis', 'host'), port=inifile.get('redis', 'port'))

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis
Session(app)


    
@app.route('/')
def index():
  return render_template("index.html", title="hello")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
