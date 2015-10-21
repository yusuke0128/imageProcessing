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
alpha = 0.7
beta = 0.5   

gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
gimg = cv2.adaptiveThreshold(gimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
gimg = cv2.medianBlur(gimg,5)
gimg = cv2.cvtColor(gimg,cv2.COLOR_GRAY2BGR)  

Z = img.reshape((-1,3))
Z = np.float32(Z)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 5
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
center = np.uint8(center) 
res = center[label.flatten()] 
res2 = res.reshape((img.shape))
res2 = cv2.medianBlur(res2,5)

art = cv2.addWeighted(gimg,alpha,res2,beta,0)
artName = raw_input('please fileName after artFilter ') 

cv2.imwrite(artName,art)

