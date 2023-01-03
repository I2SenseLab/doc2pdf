from flask import Flask, request, send_file
from documentCreation import convert_to
import os 
import tempfile

app = Flask(__name__)
app.secret_key = 'thereisacatinthemiddleoftown'
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/convert_doc_to_pdf", methods=['POST'])
def convert_doc_to_pdf():
    print("Converting Document To PDF")

    if request.method == 'POST':
        #Create a temporary file for the document
        file_name = next(tempfile._get_candidate_names())
        file_path = os.path.join(tempfile.gettempdir(), file_name)

        f= request.files['file']
        f.save(file_path)


        try:
            file_path = convert_to(tempfile.gettempdir(),file_path)
        except:
            file_path = "BADPDF.pdf"

        response = send_file(
            file_path,
            mimetype='image/png',
            as_attachment=True,
            download_name='file.pdf'
        )

        return response
    else:
        return "Not a post request"

@app.route("/")
def running():

    return "Request Recieved"


if __name__ == "__main__":
    content = ("MDAcert.pem","MDAkey.pem")
    app.run(ssl_context=content,debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 80)))