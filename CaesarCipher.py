from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

LOGO_FOLDER = os.path.join('static', 'crypt_logo')
app.config['UPLOAD_FOLDER'] = LOGO_FOLDER
img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'cryptlogo.jpg')

@app.route('/')
def mainPage():
    img_path = os.path.realpath('cryptlogo.jpg')
    return render_template('test.html', logo = img_filename)

@app.route('/encrypt.html')
def encryptionPage():
    return render_template('encrypt.html', logo = img_filename)

@app.route('/decrypt.html')
def decryptionPage():
    return render_template('decrypt.html', logo = img_filename)

@app.route('/enc')
def encrypt():
    plain_text = request.args.get('ptext')
    key = int(request.args.get('key'))
    low_case = 'abcdefghijklmnopqrstuvwxyz'
    up_case = low_case.upper()
    cipher_text = ''

    for char in plain_text:
        if char in low_case:
            cipher_text += low_case[(low_case.find(char) + key )%26]

        elif char in up_case:
            cipher_text += up_case[(up_case.find(char) + key )%26]

        else:
            cipher_text += char

    return render_template('encrypted.html',msg = cipher_text)
    # return cipher_text

@app.route('/dec')
def decrypt():
   cipher_text = request.args.get('ctext')
   key = int(request.args.get('key'))
   low_case = 'abcdefghijklmnopqrstuvwxyz'
   up_case = low_case.upper()
   plain_text = ''

   for char in cipher_text:
      if char in low_case:
        plain_text += low_case[(low_case.find(char) - key )%26]

      elif char in up_case:
        plain_text += up_case[(up_case.find(char) - key )%26]

      else:
         plain_text += char

   return render_template('decrypted.html',msg = plain_text)


if __name__ == '__main__':
    app.run(debug = True)
