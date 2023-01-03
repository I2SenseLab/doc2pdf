from flask import Flask, request, send_file
from documentCreation import convert_to
import os 
import tempfile

app = Flask(__name__)

@app.route("/convert_doc_to_pdf", methods = ['GET', 'POST'])
def convert_doc_to_pdf():
    print("Converting Document To PDF")

    if request.method == 'POST':
        #Create a temporary file for the document
        file_name = next(tempfile._get_candidate_names())
        file_path = os.path.join(tempfile.gettempdir(), file_name)

        f= request.files['file']
        f.save(file_path)
        return "POST MADE"
    else:
       


        return "This function expects a POST of a file"
#         try:
#             file_path = convert_to(tempfile.gettempdir(),file_path)
#         except:
#             file_path = "BADPDF.pdf"

#         response = send_file(
#             file_path,
#             mimetype='image/png',
#             as_attachment=True,
#             download_name='file.pdf'
#         )

#         return response
#     else:
#         return "Not a post request"

@app.route("/")
def running():


    return "DOCX - PDF Conversion Service Running"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))