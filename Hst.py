import cv2
import pylab as plt
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

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.show()
