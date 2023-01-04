from flask import Flask, request, send_file
from documentCreation import convert_to
import os 
import tempfile
import traceback
app = Flask(__name__)

@app.route("/convert_doc_to_pdf", methods = ['GET', 'POST'])
def convert_doc_to_pdf():
    print("Converting Document To PDF")

    if request.method == 'POST':
        #Create a temporary file for the document
        file_name = next(tempfile._get_candidate_names())
        file_path = os.path.abspath(os.path.join(tempfile.gettempdir(),file_name))
        print("Made File Path: ",file_path)
        try:
            if 'file' not in request.files:
                print("File Not in File Request")
                return "No File Uploaded Recognized: " + request
            else:
                print("Saving File From Request: ", file_path)
                f= request.files['file']
                f.save(file_path)
                print("Validating the File has been saved: ", os.path.exists(file_path))
                try:
                    #file_path = "BADPDF.pdf"
                    
                    file_path = convert_to(file_path)
                    print("Converted File Name ",file_path)
                except:
                    file_path = "BADPDF.pdf"
                    traceback.print_exc()
                    print("Excepted File Converion Failed")


                print("Returning the following file, ", file_path)
                response = send_file(
                    file_path,
                    mimetype='application/pdf',
                    as_attachment=True,
                    download_name='file.pdf'
                )

                return response

        except:
            print("Failed to Save File")
            return "File Upload Failed"

    else:
       


        return "This function expects a POST of a file"




#         return response
#     else:
#         return "Not a post request"

@app.route("/")
def running():


    return "DOCX - PDF Conversion Service Running"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))