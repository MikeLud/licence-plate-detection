# licence-plate-detection

In recent years, licence plate detection has been one of the useful approaches for vehicle surveillance.In this project, I will use use YOLOV5 model to detect number plate from a frame

## Functionality

	1. Break video into frames, if not image
	2. Detect car and number plate from frames using api based on yolov5
		2.a Functionality of api:
			2.a.1. Takes image as request
			2.a.2. Make prediction to detect car and number plate 
			2.a.3. Return base64 image and predicted bounding boxes as response
	3. Display the results on UI
		Link : 34.93.166.166:5000/licence-plate-detection/
	
		
## Its Application

Traffic control and the identification of vehicle owners have become a major problem in all countries. Sometimes it becomes difficult to identify a vehicle owner who is breaking the rules of the road and driving too fast. Therefore, it is not possible to catch and punish such kind of people because the traffic personnel might not be able to retrieve the vehicle number of the moving vehicle due to the speed of the vehicle. So to solve these types of problems we need to create a Licence Plate Detection System.

### Following are the steps to use this repository
	
	1. git clone https://github.com/mohammadnoorulhasan/licence-plate-detection.git
	2. cd licence-plate-detection
	3. pip install -r requirements.txt
	4. python app.py
	
Once you run the above our API is hosted on X.X.X.X:PORT 

	5. Open above api server on web browser or alternativily you can use POSTMAN to send request, below is the output from browser
	
![image](https://user-images.githubusercontent.com/45382896/142477710-c8388526-0ab4-4bef-9497-701889795578.png)

	If you want to use this API in your code you can integrate using below
	
	Request end point:
		URL 	:	http://34.93.166.166:5000/licence-plate-detection/image
		Method	:	POST
	
	Request
		type	:	form-data
		key	:	file
		value	:	image-file
		
	Respose :
	{
		base64 		: its a image converted in base64 format on which bounding box is already drawn
		confidence	: with how much confidence a class is detected
		name		: name of the classes
		object_found	: True/False
		status		: Status from api
		xmax		: X cordinate whear target is found
		xmin		: width of the target from X cordinate
		ymax		: Y cordinate whear target is found
		ymax		: width of the target from Y cordinate
	}

	6. Once you upload image and select type of response
		a. JSON - It'll return following data in JSON format
			
		b. HTML template - It will redirect to HTML page which contains resulted image
		
![image](https://user-images.githubusercontent.com/45382896/142479193-2231dce2-a4d8-4884-a755-7795458240fd.png)
