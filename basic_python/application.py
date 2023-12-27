import sys
import os 
import flask 

application = flask.Flask(__name__)

@application.route('/')
def hello_world():
    return flask.jsonify({
        'name': 'flaskapp',
        'python_version': sys.version.split(" ", 2)[0],
        'environment': os.environ.copy(),
        'flask_version': flask.__version__,
        'pre-build': get_command_content('pre-build'),
        'post-build': get_command_content('post-build'),
        'build': get_command_content('build'),
        'pre-run': get_command_content('pre-run'),
    })

def get_command_content(command: str):
    command_content = 'error: file not exist'
    if os.path.exists(f"{command}.txt"):
        with open(f"{command}.txt", "r") as f:
            command_content = f.read()
    return command_content
    
    

if __name__ == '__main__':
    port = int(os.environ.get("FLASK_RUN_PORT", 8000))
    application.run(host='0.0.0.0', debug=False, port=port)
