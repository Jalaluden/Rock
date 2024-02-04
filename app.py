from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    password_length = int(request.form['password_length'])
    use_lowercase = 'use_lowercase' in request.form
    use_uppercase = 'use_uppercase' in request.form
    use_digits = 'use_digits' in request.form
    use_special_chars = 'use_special_chars' in request.form

    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return render_template('index.html', error='Select at least one character set for the password.')

    generated_password = generate_random_password(password_length, characters)
    return render_template('index.html', generated_password=generated_password)

def generate_random_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    app.run(debug=True)
