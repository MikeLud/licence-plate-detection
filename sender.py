import requests
import json
import cv2
import numpy as np
addr = 'http://127.0.0.1:8000/'
test_url = addr + 'licence-plate-detection/pixel'

# prepare headers for http request
# content_type = 'image/jpeg'
# headers = {'content-type': content_type}

img = cv2.imread('dataset/test/images/b1a50a3824887ee2.jpg')
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
print(img_encoded)
# send http request with image and receive response
# response = requests.post(test_url, data=img_encoded.tostring())
# decode response
# print(response.text)