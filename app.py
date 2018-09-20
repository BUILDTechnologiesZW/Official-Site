from flask import Flask, render_template, url_for
import gunicorn


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/systems')
def systems():
    return render_template('systems.html')

@app.route('/mobile')
def mobile():
    return render_template('mobile.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    