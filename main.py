from flask import Flask, request


app = Flask(__name__)
app.secret_key = 'thereisacatinthemiddleoftown'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/certificate")
def certificateHandler():
    print(request)
    return request


if __name__ == "__main__":
    content = ("MDAcert.pem","MDAkey.pem")
    app.run(ssl_context=content,debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))