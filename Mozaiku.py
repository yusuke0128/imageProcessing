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
oimg = img  
origsize=img.shape[:2][::-1]

img = cv2.resize(img, (origsize[0]/5,origsize[1]/5))
img = cv2.resize(img, origsize)
cv2.imshow('Orignal',oimg) 
cv2.imshow('Mozaiku',img)
print'Press any key to exit.'
cv2.waitKey(0)  
