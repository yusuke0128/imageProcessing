import cv2
import pylab as plt
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

bcp = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
bcpName = raw_input('please fileName after bcp ') 
cv2.imwrite(bcpName,bcp)


