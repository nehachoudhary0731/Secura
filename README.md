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

#Sample Test
1. Run the App
Open terminal and run: python app.py

2.Open in Browser
- Follow the URL displayed in terminal
  
3.Encrypt a File
   - On the **Home Page**, upload a file.
   - Click the **Encrypt** button. And download Encrypted file and key file.
     
4.Decrypt the File
   - Go to the **Decrypt Page**.
   - Upload both:
     - Encrypted file
     - Key file
   - Click **Decrypt**. And Download the decrypted file.
5. **Back to Home**

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


   
