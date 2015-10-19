import cv2
import sys  
  
argvs=sys.argv  
if (len(argvs) != 2):  
    print 'Usage: # python %s filename' % argvs[0]  
    quit()   
  
imagefilename = argvs[1]  
try:  
    img=cv2.imread(imagefilename, 1)  
except:  
    print 'faild to load %s' % imagefilename  
    quit()   

cascade_path = "/home/yusuke/opencv-3.0.0/data/haarcascades/haarcascade_frontalface_alt2.xml"

color = (255, 255, 255) 

gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
cascade = cv2.CascadeClassifier(cascade_path)
 
facerect = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
 
if len(facerect) > 0:
 
  for rect in facerect:
    cv2.rectangle(img, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
else:
  print("no face")
   
faceScanName = raw_input('please fileName after faceScan') 
cv2.imwrite(faceScanName,img)
 
