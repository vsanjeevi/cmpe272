
from flask import Flask

app = Flask(__name__)  #configures Flask to load associated files

from app import routes #app is Flask instance in this package

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)