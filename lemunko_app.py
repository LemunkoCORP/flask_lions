from flask import Flask
from blueprints import base_blueprint

app = Flask(__name__)
app.register_blueprint(base_blueprint.page)
#admetricks.register_blueprint(base.page)

#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello World!'

if __name__ == '__main__':
    app.run()
