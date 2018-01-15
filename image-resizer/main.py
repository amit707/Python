import cv2 #import cv2liabrary for object detections
import glob #import glob liabrary to select the patterns files within that folder
images=glob.glob("*.jpg")#to read all images with any name and with .jpg extention and put them in a list

for image in images:
	img=cv2.imread(image,0)#read image in gray scale
	re=cv2.resize(img,(500,500))#resize the image with pixels 500x500
	cv2.imshow("Hey",re)#show the image using imshow method on Hey frame
	cv2.waitKey(1000)#window will be opened for 1 second
	cv2.destroyAllWindows()#destroy the opened window after 1 second
	cv2.imwrite("resized"+image,re)#save's the each file with name as resized_filename