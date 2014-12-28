import os
from flask import Flask, request, session, g, \
    render_template, flash
from werkzeug import secure_filename

UPLOAD_FOLDER = 'static/music/'
ALLOWED_EXTENSIONS = set(['mp3', 'wav'])


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
      filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return render_template('thankyou.html')
  return render_template('index.html')

@app.route('/music')
def display_music():
  files = os.listdir('static/music')
  return render_template('music.html', files=files)

@app.route('/music/<filename>')
def play_song(filename):
  return render_template('playsong.html', song=filename)

app.run(host='0.0.0.0', port=8000)
