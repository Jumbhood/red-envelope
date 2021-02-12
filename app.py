from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    title = "Open Your 2021 Red Evenlope!"
    return render_template('index.html', title = title)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug='True')