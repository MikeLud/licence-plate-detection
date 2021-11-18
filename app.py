# Import necessary modules

import torch
from flask import Flask, request, jsonify, render_template
from PIL import Image
import cv2
import numpy as np
import base64
import yaml
from yaml.loader import SafeLoader
from io import BytesIO
# Loading configuration of the model and api
# Add execptional handling
try:
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)
except:
    print("File not found")
    config = {}

if "project_name" in config.keys():
    project_name = config["project_name"]
else:
    project_name = "new"

if "output_path" in config.keys():
    output_path = config["output_path"]
else:
    output_path = "output"



if "model_name" in config.keys():
    model_name = config["model_name"]
else:
    model_name = "yolov5s"

if "weight_path" in config.keys():
    weight_path = config["weight_path"]

if "host_name" in config.keys():
    host_name = config["host_name"]
else:
    host_name = "0.0.0.0"

if "port_number" in config.keys():
    port_number = config["port_number"]
else:
    port_number = "8000"

output = "templates/"

app = Flask(__name__, static_folder="templates/")

if model_name == "custom":
    model = torch.hub.load('ultralytics/yolov5', model_name, path = weight_path)
else:
    model = torch.hub.load('ultralytics/yolov5', model_name)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route(f'/{project_name}/image', methods = ['GET', 'POST'])
def detect_licence_plate_from_image():
    if request.method == 'POST':
        
        f = request.files['file']
        response_type =  request.form.get("response-type")
        print("response_type:", response_type)
        img = Image.open(f)
        result = model(img, size = 1024)
        response = generate_response(result)
        if response_type == "JSON":
            return jsonify(response)
        
        else:
            
            return render_template("response.html", image_path = f"../{output}image0.jpg")

@app.route(f'/{project_name}/pixel', methods = ['GET', 'POST'])
def detect_licence_plate_from_pixel():
    if request.method == 'POST':
        r = request
        nparr = np.fromstring(r.data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        result = model(img)
        response = generate_response(result)
        return jsonify(response)
		

def generate_response(result):
    keys = ["xmin", "ymin", "xmax", "ymax", "confidence", "name"]
    response = {}
    bboxes = result.pandas().xyxy[0]
    bboxes = bboxes[bboxes["confidence"] >= 0.5]
    result.save(save_dir = f"{output}")

    with open(f"{output}image0.jpg", "rb") as image_file:
        b64 = base64.b64encode(image_file.read()).decode('utf-8')

    # for img in result.imgs:
    #     buffered = BytesIO()
        
    #     img_base64 = Image.fromarray(img)
    #     # img_base64.save(f"{output}/output.png")
    #     img_base64.save(buffered, format="JPEG")
    #     b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')  # base64 encoded image with results

    for key in keys:
        # print(bboxes[key].reset_index(True))
        response[key] = bboxes[key].tolist()
    response["object_found"] = bool(len(bboxes))
    response["status"] = "Success"
    response["base64"] = b64
    return response

if __name__ == '__main__':
       app.run(debug = True, port = port_number, host = host_name)






# try: pass
# expect Exception as e: 
#   click.secho(f"Exception raised : {e}, error online : {sys.exc_info()[-1].tb_lineno}, in file : {os.path.basename(_file_)} ", fg= "red")