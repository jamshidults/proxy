from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
# import win32print
import os
# from waitress import serve



app = Flask(__name__)
CORS(app)

TEMPPRINT_FILE = 'tempprint.txt'

def create_default_files():
    """
    Generate default files for the API server
    :return:
    """


    if not os.path.exists(TEMPPRINT_FILE):
        fp = open(TEMPPRINT_FILE, 'x', encoding="us-ascii")  # pylint: disable=invalid-name,consider-using-with
        fp.close()


@app.route('/dotmatrix/print', methods=['POST'])
def dotmatrix_print():
    printer_data = request.form['printer_data']
    log_file = open(TEMPPRINT_FILE, 'w', encoding="us-ascii")  # pylint: disable=consider-using-with
    log_file.write(printer_data)
    log_file.write('\n')  # ASCII with line terminator
    log_file.close()
    os.startfile(TEMPPRINT_FILE, "print")
    
    # p = win32print.OpenPrinter(PRINTER_NAME)
    #
    #
    # job = win32print.StartDocPrinter(p,1,("DOTMATRIX",None,"RAW"))
    # win32print.StartPagePrinter(p)
    # win32print.WritePrinter(p,printer_data.encode() )
    # win32print.EndPagePrinter(p)
    # win32print.EndDocPrinter(p)
    # win32print.ClosePrinter(p)
    
    return jsonify({'status': 'OK'})
if __name__ == '__main__':
    create_default_files()

# if __name__ == "__main__":
#
#     # serve(app, host="127.0.0.1", port=8000)