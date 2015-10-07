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
  
#define small image size  
imgsize=img.shape  
  
#imgsize = (height,width,depth)  
  
simg_width=imgsize[1]/2  
simg_height=imgsize[0]/2  
  
#half size image and grayscaled image  
simg=cv2.resize(img,(simg_width,simg_height))  
gimg=cv2.cvtColor(simg,cv2.COLOR_BGR2GRAY)  
himg=cv2.cvtColor(simg,cv2.COLOR_BGR2HSV)
cv2.imshow('Half size',simg)  
cv2.imshow('Grayscaled',gimg)  
cv2.imshow('sobelFiltter',himg)
  
print 'Press any key to exit.'  
cv2.waitKey(0)  
