#-*-coding:utf-8-*-
import cv2
import pylab as plt
import sys
import matplotlib.font_manager

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

hist = img.ravel()
plt.hist(hist,256,[0,256])
plt.xlim([0,256])
fontprop = matplotlib.font_manager.FontProperties(fname="/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")
plt.title(u"ヒストグラム", fontdict = {"fontproperties": fontprop})
plt.xlabel(u"輝度値", fontdict = {"fontproperties": fontprop})
plt.ylabel(u"画素数", fontdict = {"fontproperties": fontprop})
plt.show()
