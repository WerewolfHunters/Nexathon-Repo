from flask import Flask, render_template, request, send_from_directory
from poster_designer import generate_poster
import json
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['STATIC_FOLDER'] = 'static'  # Add this line to specify the static folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    title = request.form['title']
    event_title = request.form['event_title']
    venue = request.form['venue']
    
    img_path = generate_poster(title=title, event_title=event_title, venue=venue)  # Passing event_title and venue to generate_poster()
    
    return json.dumps({'success': True, 'img_path': img_path})

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
