from flask import Flask, render_template, request, redirect, url_for, abort
from helpers import extract_poses, save_angles
import time
import os

if not os.path.exists('uploads'):
    os.mkdir('uploads')
if not os.path.exists('processed_cache'):
    os.mkdir('processed_cache')

app = Flask(__name__, static_folder='./templates/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    print(request.form)
    if request.method == 'POST':
        print("Logging in ")
        username = request.form['email']
        password = request.form['password']
        # check if the username and password are correct
        if username == 'admin@admin.com' and password == 'admin':
            return redirect(url_for('upload_image'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('index.html', error=error)
    else:
        abort(403)

@app.route('/upload_image', methods=['POST', 'GET'])
def upload_image():
    if request.method == 'POST':
        image = request.files['image']
        print(image)
        if image:
            filename = str(time.time())
            image.save(f'./uploads/{filename}.jpg')
            extract_poses(f'./uploads/{filename}.jpg')

        return redirect(url_for('upload_image'))
    else:
        return render_template('upload_screen.html')



if __name__ == '__main__':
    app.run(debug=True)