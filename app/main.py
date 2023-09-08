from flask import Flask, request, jsonify, render_template, send_file
from pydub import AudioSegment
import numpy as np
import deepspeech
import soundfile as sf
from io import BytesIO

app = Flask(__name__)
model = deepspeech.Model('/app/models/deepspeech-0.9.3-models.pbmm')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['audio']
    file_extension = audio_file.filename.split('.')[-1]
    
    if file_extension.lower() not in ['wav', 'mp3']:
        return jsonify({"error": "Invalid file type"}), 400
    
    audio_data = audio_file.read()
    audio = AudioSegment.from_file(BytesIO(audio_data), format=file_extension)
    
    # DeepSpeech expects 16-bit mono PCM
    if audio.channels > 1:
        audio = audio.set_channels(1)
    if audio.frame_rate != 16000:
        audio = audio.set_frame_rate(16000)
    
    text = model.stt(np.frombuffer(audio.raw_data, np.int16))
    
    # Save the transcribed text to a file
    with open("transcribed_text.txt", "w") as text_file:
        text_file.write(text)
        
    return send_file('transcribed_text.txt', as_attachment=True, download_name='transcribed_text.txt')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
