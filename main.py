from flask import Flask, request


app = Flask(__name__)
app.secret_key = 'thereisacatinthemiddleoftown'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/certificate")
def certificateHandler():
    print(request)