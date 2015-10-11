import cv2
import numpy as np
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
  
fimg = np.fft.fft2(img)

fimg = np.log(np.abs(fimg) + 1)

fimg = fimg / np.amax(fimg) * 255
FFT2DName = raw_input('please fileName after FFT ') 
cv2.imwrite(FFT2DName,fimg)
