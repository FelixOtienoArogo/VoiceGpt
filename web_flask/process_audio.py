from flask import jsonify, request

def process_audio():
    """Takes in the voice message from the frontend and process it"""
    try:
        #Get the audio file from the request
        audio_file = request.files['audio']
        return jsonify({'status': 'success', 'message': "Audio processing complete"})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

