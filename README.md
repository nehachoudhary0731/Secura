#  Secura – Secure File Encryption & Decryption Web App

Secura is a lightweight Flask-based web application designed for secure "file encryption and decryption".
The goal of this project was to create a simple, clean UI to demonstrate the complete end-to-end functionality of encrypting and 
decrypting files using dynamically generated unique keys.

# Project Highlights

-  Encrypt any file securely using a unique Fernet key
-  Download the "key file" immediately after encryption
-  Decrypt encrypted files by uploading both:
- The encrypted .enc file
- The correct .key file
-  Download decrypted file after successful decryption
-  Files are stored and served from secure folders:
- uploads/ → Original uploaded files
- encrypted/ → Encrypted files with .enc extension
- decrypted/ → Final decrypted output files
- keys/ → Stored key files used for decryption
-  Functional and tested on local environment with Flask
- Here i build simple UI to test the functinality of backend using html and css
  
# Tech Stack
- Python 3
- Flask (web framework)
- Fernet from cryptography module
- HTML5 + CSS3 (For Basic UI Styling)

#sample test
-run app.py in terminal like python app.py
-follow given url 
-Go to HomePage upload file then click encrypt and download encrypt file along with key.
-Then Decrypt encrypted file by uploading both encrypted and key file.
- Download Decrypted file and back to home 

#Project Structure

Secura/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── uploads/        ( Stores uploaded files)
├── encrypted/      (Stores encrypted files)
├── decrypted/      (Stores decrypted files)
├── keys/           (Stores generated key files)


   
