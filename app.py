from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/hello/<name>')
def green(name):
    return render_template('green.html', name = name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
