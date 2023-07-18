import cv2  
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
from flask import Flask, request, render_template, redirect,jsonify
import urllib.request
from englisttohindi.englisttohindi import EngtoHindi

#from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
#cred = credentials.Certificate('key.json')
#default_app = initialize_app(cred)
#db = firestore.client()
#todo_ref = db.collection('todos')

#app.config["IMAGE_UPLOADS"] = "C:/Users/Sathvik/Downloads/OCR/images"
# app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG"]

from werkzeug.utils import secure_filename


#image_file = "images/vc2.png"
#img = cv2.imread(image_file)
@app.route('/', methods=["GET", "POST"])


def upload_image():

    global img
    try:
        reqRef = request.get_json(force=True)
        img = reqRef["imgUrl"]
        urllib.request.urlretrieve(img,"gfg.jpeg")
    # img = Image.open("gfg.jpeg")
    # img.show()

    # print("abc"+ img)
    
        
        
        path_to_tesseract=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        #Imagepath='gfg.jpeg'
        pytesseract.tesseract_cmd=path_to_tesseract
        text=pytesseract.image_to_string(Image.open("gfg.jpeg"))
        res = EngtoHindi(text)

        return jsonify({
            #"ocr_result": text,
            "hindi_result": res.convert,

        })

    except Exception as e:
        return jsonify({
            "weigthURL": "No found",
            "error": str(e)
        })
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
