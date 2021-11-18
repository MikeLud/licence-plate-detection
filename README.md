# licence-plate-detection

In recent years, licence plate detection or license plate recognition has been one of the useful approaches for vehicle surveillance.In this project, I will use use YOLOV5 model to detect number plate from a frame

## Its Application

Traffic control and the identification of vehicle owners have become a major problem in all countries. Sometimes it becomes difficult to identify a vehicle owner who is breaking the rules of the road and driving too fast. Therefore, it is not possible to catch and punish such kind of people because the traffic personnel might not be able to retrieve the vehicle number of the moving vehicle due to the speed of the vehicle. So to solve these types of problems we need to create a Licence Plate Detection System

### Following are the steps to use this repository
	
	1. git clone https://github.com/mohammadnoorulhasan/licence-plate-detection.git
	2. cd licence-plate-detection
	3. pip install -r requirements.txt
	4. python app.py
	
Once you run the above our API is hosted on X.X.X.X:PORT 

	5. Open above api server on web browser, below is the output 
	
	![image](https://user-images.githubusercontent.com/45382896/142477710-c8388526-0ab4-4bef-9497-701889795578.png)

	Or alternativily you can use POSTMAN to send request
	
	6. Once you upload image and select type of response
		a. JSON - It'll return following data in JSON format
			a.1. base64 	: its a image converted in base64 format on which bounding box is already drawn
			a.2. confidence	: with how much confidence a class is detected
			a.3. name	: name of the classes
			a.4. object_found	: True/False
			a.5. status		: Status from api
			a.6. xmax		: X cordinate whear target is found
			a.7. xmin		: width of the target from X cordinate
			a.8. ymax		: Y cordinate whear target is found
			a.9. ymax		: width of the target from Y cordinate
		b. HTML template - It will redirect to HTML page which contains resulted image
		
			![image](https://user-images.githubusercontent.com/45382896/142479193-2231dce2-a4d8-4884-a755-7795458240fd.png)
