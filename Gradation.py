#-*-coding:utf-8-*-
import cv2
import numpy as np
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

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gradationNum = input('何階調にしますか?')
width = img.shape[0]
height = img.shape[1]
temp = np.zeros_like(img)
for i in range(1,gradationNum):
 for j in xrange(width):
  for k in xrange(height):
   if img[j,k]>(256/gradationNum)*i: 
    temp[j,k] += (256/gradationNum)*i
GraditionName = raw_input('please fileName after GraditionTransformation') 
cv2.imwrite(GraditionName,temp)
