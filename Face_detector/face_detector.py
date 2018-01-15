import cv2 #import the cv2 package to perform object detection

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #include xml file which has all the attributes for detecting the faces


img=cv2.imread("new.jpg")#imread method for reading the image and then pass the url of that image

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#to convert the color image into gray colored image 

faces=face_cascade.detectMultiScale(gray_img,
	scaleFactor=1.12,
	minNeighbors=5)#use detectMultiScale method to detect the faces,scalefactor defines what percentage should be the next iteration of the base value,minNeighbors specifies the min neighbors together


for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)#display each faces from img
print(type(faces))#print the type of faces,it is numpy.ndarray
print(faces)#print the values of faces

resized=cv2.resize(img,(int(img.shape[1]/4),int(img.shape[0]/4)))#resize the original image 
cv2.imshow("Gray",resized)#show the resized image with frame title as Gray
cv2.waitKey(0)#to hold the window,since it is 0 then it will be remained open till we won't press any key
cv2.destroyAllWindows()#it is used to destroy all windows