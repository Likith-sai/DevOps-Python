import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Password generator function
def generate_password(passlen):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    if passlen <= 0:
        return ""
    if passlen > len(s):
        return "Password length exceeds character set size."
    return "".join(random.sample(s, passlen))

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        try:
            passlen = int(request.form['passlen'])
            password = generate_password(passlen)
        except ValueError:
            password = "Invalid input. Please enter a valid number."
    return render_template('index.html', password=password)

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
