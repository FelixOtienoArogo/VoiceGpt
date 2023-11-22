from flask import *
# from flask_cors import CORS
# from .process_audio import process_audio

app = Flask(__name__, template_folder='./templates')
# CORS(app) # Enable CORS for all routes

@app.route('/', strict_slashes=False)
def home():
    """ Prints a Message when / is called """
    return render_template('test.html')



# @app.route('/process_audio', strict_slashes=False, methods=['POST'])
# def process_audio_route():
#     return process_audio()

if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port= 5000, debug=True)
