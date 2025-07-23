#made with flask all importing are here
#this is the main entry points of the secura app
#and these are module which is required

from flask import Flask, render_template, request, send_file
from cryptography.fernet import Fernet
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define directories(this folders will store files based on their stage)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'maintenance/uploads')
ENCRYPTED_FOLDER = os.path.join(BASE_DIR, 'maintenance/encrypted')
DECRYPTED_FOLDER = os.path.join(BASE_DIR, 'maintenance/decrypted')
KEY_FOLDER = os.path.join(BASE_DIR, 'maintenance/keys')

#here it will Create folders if not exist

for folder in [UPLOAD_FOLDER, ENCRYPTED_FOLDER, DECRYPTED_FOLDER, KEY_FOLDER]:
    os.makedirs(folder, exist_ok=True)

#this is home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST']) #this is encrypt 
def encrypt_file():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        key = Fernet.generate_key()
        cipher = Fernet(key)

        with open(file_path, 'rb') as f:
            original_data = f.read()

        encrypted_data = cipher.encrypt(original_data)
        enc_filename = filename + '.enc'
        encrypted_path = os.path.join(ENCRYPTED_FOLDER, enc_filename)

        with open(encrypted_path, 'wb') as f:
            f.write(encrypted_data)

        key_filename = filename + '.key'
        key_path = os.path.join(KEY_FOLDER, key_filename)

        with open(key_path, 'wb') as f:
            f.write(key)

        return render_template('result.html',
                               operation='Encryption',
                               file_path=encrypted_path,
                               key_path=key_path,
                               filename=os.path.basename(encrypted_path),
                               keyname=os.path.basename(key_path))
    return "No file uploaded."

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    enc_file = request.files['enc_file']
    key_file = request.files['key_file']

    if enc_file and key_file:
        enc_filename = secure_filename(enc_file.filename)
        key_filename = secure_filename(key_file.filename)

        enc_path = os.path.join(ENCRYPTED_FOLDER, enc_filename) # it save file to decrypted folder
        key_path = os.path.join(KEY_FOLDER, key_filename)

        enc_file.save(enc_path)
        key_file.save(key_path)

        with open(enc_path, 'rb') as ef:
            encrypted_data = ef.read()

        with open(key_path, 'rb') as kf:
            key = kf.read()

        try:
            cipher = Fernet(key)
            decrypted_data = cipher.decrypt(encrypted_data)
        except Exception as e:
            return f"Decryption failed: {str(e)}"

        # Remove .enc for output file
        original_name = enc_filename.replace('.enc', '')
        decrypted_path = os.path.join(DECRYPTED_FOLDER, original_name)

        with open(decrypted_path, 'wb') as df:
            df.write(decrypted_data)

        return render_template('result.html',
                               operation='Decryption',
                               file_path=decrypted_path,
                               filename=os.path.basename(decrypted_path))
    return "Both files required."

@app.route('/download/<path:filename>') #here it will download the route
def download(filename):
    full_path = None
    for folder in [ENCRYPTED_FOLDER, DECRYPTED_FOLDER, KEY_FOLDER]:
        trial = os.path.join(folder, filename)
        if os.path.exists(trial):
            full_path = trial
            break
    if full_path:
        return send_file(full_path, as_attachment=True)
    return "File not found.", 404

if __name__ == '__main__': #(it run flask)
    app.run(debug=True)
