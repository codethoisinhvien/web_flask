from flask import Flask

from src.api.user_authentication import user_authentication
from src.api.user import user
from src.api.subject import subject
from src.api.exam import exam
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
@app.route('/')
def hello_world():
    return 'Giangs'
app.register_blueprint(user_authentication, url_prefix='/api')
app.register_blueprint(exam, url_prefix='/api')
app.register_blueprint(subject, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True,host='192.168.0.101' , port=5000)
