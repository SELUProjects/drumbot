from flask import Flask
from drumbot.drumbot import drumbot

app = Flask(__name__)
app.register_blueprint(drumbot, url_prefix='/')

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.debug = True
    app.run(host='0.0.0.0', port=80)

