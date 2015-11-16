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
 img=cv2.imread(imagefilename, 0)  
except:  
 print 'faild to load %s' % imagefilename  
 quit()   
 
img = cv2.equalizeHist(img)
HistogramEqualizationName = raw_input('please fileName after HistogramEqualization') 
cv2.imwrite(HistogramEqualizationName,img)  
                   
