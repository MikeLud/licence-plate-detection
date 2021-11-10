import torch

def create_dict(bboxes):
    keys = ["xmin", "ymin", "xmax", "ymax", "confidence", "name"]
    response = {}


    print(len(bboxes),end="\n\n")
    for key in keys:
        # print(bboxes[key].reset_index(True))
        response[key] = bboxes[key].tolist()
    response["object_found"] = bool(len(bboxes))
    response["status"] = "Success"
    print(response)

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'F:\Machine Learning\yolo\global-wheat-detection\\test\\2fd875eaa.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img = "F:\Machine Learning\yolo\licence-plate-detection\dataset\\test\images\\b1a50a3824887ee2.jpg"
# img = [img1, img2]
# Inference
results = model(img, size = 1024)
p = results.pandas().xyxy[0]

print(p)
# print("p",len(p))
# print("\n------\n")
# for i in p:
#     for j in i:
#         print(i[j],end = "------\n")

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.


create_dict(p)