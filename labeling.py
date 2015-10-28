import cv2
import numpy as np 
import random
import copy
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

height, width = img.shape[:2]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
em,bcp = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
n,labelImg = cv2.connectedComponents(bcp)
dst = copy.copy(img)
colors = []

for i in range(1,n+1):
 colors.append(np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))

for y in range(0,height):
 for x in range(0,width): 
  if labelImg[y,x] > 0:
   dst[y,x] = colors[labelImg[y,x]]
  else:
   dst[y,x] = [0,0,0]
labelingName = raw_input('please fileName after labeling') 
cv2.imwrite(labelingName,dst)
