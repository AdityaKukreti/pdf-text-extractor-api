from flask import Flask,request,jsonify
from pdfReader import PDFReader
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
pdfReader = PDFReader()

try:
    path = os.path.dirname(os.path.abspath(__file__))
    upload_folder=os.path.join(
    path.replace("/file_folder",""),"tmp")
    os.makedirs(upload_folder, exist_ok=True)
    app.config['upload_folder'] = upload_folder
except Exception as e:
    app.logger.info("An error occurred while creating temp folder")
    app.logger.error("Exception occurred : {}".format(e))
                     
@app.route('/')
def index():
    return '''
        <form method='POST' action='/extractText'>
        <input type='file' name='PDFFile'>
        <input type='submit'>
        </form>
    '''

@app.route('/extractText', methods=['POST'])
def saveData():
    
    pdf_file = request.files['file']
    pdf_name = pdf_file.filename
    save_path = os.path.join(app.config.get('upload_folder'),pdf_name)
    pdf_file.save(save_path)
    return jsonify({"text":pdfReader.getText(pdf_name)})
  


if __name__ == "__main__":
    app.run(port = 10000, host = '0.0.0.0')
