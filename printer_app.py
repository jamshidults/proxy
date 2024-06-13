PRINTER_NAME = 'TVS MSP 270 Series'
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import os
import win32print
import win32con
import win32ui


app = Flask(__name__)
CORS(app)




@app.route('/dotmatrix/print', methods=['POST'])
def dotmatrix_print():
    printer_data = request.form['printer_data']
    
    p = win32print.OpenPrinter(PRINTER_NAME)
   

    job = win32print.StartDocPrinter(p,1,("DOTMATRIX",None,"RAW"))
    win32print.StartPagePrinter(p)
    win32print.WritePrinter(p,printer_data.encode() )
    win32print.EndPagePrinter(p)
    win32print.EndDocPrinter(p)
    win32print.ClosePrinter(p)
    
    return jsonify({'status': 'OK'})
