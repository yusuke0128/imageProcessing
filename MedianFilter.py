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

ksize =input('please ksize')
median = cv2.medianBlur(img,ksize)
MedianName = raw_input('please fileName after MedianFilter') 
cv2.imwrite(MedianName,median)
