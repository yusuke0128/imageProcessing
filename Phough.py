import cv2 
import numpy as np 
import sys

argvs=sys.argv  
if (len(argvs) != 2):  
    print 'Usage: # python %s filename' % argvs[0]  
    quit()   
  
imagefilename = argvs[1]  
try:  
    img=cv2.imread(imagefilename)  
except:  
    print 'faild to load %s' % imagefilename  
    quit()  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for i in range(0,len(lines)):
 for x1,y1,x2,y2 in lines[i]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
HoughName = raw_input('please fileName after Hough') 
cv2.imwrite(HoughName,img)


