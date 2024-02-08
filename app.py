from flask import Flask, request, jsonify, render_template
import os
import glob
from base64 import b64encode

app = Flask(__name__)

def run_inference(source_image_path, driven_audio_path):
    # Replace this function with your actual inference code
    result_dir = './results'
    preprocess = 'crop'
    enhancer = 'gfpgan'
    os.system(f"python3.8 inference.py --driven_audio {driven_audio_path} \
        --source_image {source_image_path} \
        --result_dir {result_dir} --preprocess {preprocess} --enhancer {enhancer}")

def get_animation_data():
    results = sorted(glob.glob('./results/*.mp4'))
    if results:
        mp4_name = results[-1]
        mp4 = open(mp4_name, 'rb').read()
        data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
        return mp4_name, data_url
    else:
        return None, None

@app.route('/')
def index():
    return 'Welcome to the Deepfake API'

@app.route('/choose_image', methods=['POST'])
def choose_image():
    selected_image_name = request.form['selected_image']
    return jsonify({'selected_image': selected_image_name})

@app.route('/run_inference', methods=['POST'])
def run_inference_endpoint():
    selected_image_name = request.json['selected_image']
    source_image_path = f'examples/source_image/{selected_image_name}.jpg'
    driven_audio_path = 'examples/driven_audio/RD_Radio31_000.wav'
    run_inference(source_image_path, driven_audio_path)
    return jsonify({'message': 'Inference completed successfully'})

@app.route('/display_animation')
def display_animation():
    mp4_name, data_url = get_animation_data()
    if mp4_name and data_url:
        return render_template('animation.html', mp4_name=mp4_name, data_url=data_url)
    else:
        return render_template('no_animation.html')  # Render a template indicating no animation available

if __name__ == '__main__':
    app.run()
