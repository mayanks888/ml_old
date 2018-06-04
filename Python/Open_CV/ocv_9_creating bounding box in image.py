import cv2
import numpy as np
# bounding box
'''<xmin>284</xmin>
<ymin>58</ymin>
<xmax>363</xmax>
<ymax>128</ymax>'''
# top=(284,128)
# bottom=(363,58)
top=(490,220)
bottom=(545,178)
top1=(490+50,220)
bottom1=(545+50,178)
# bottom=(400,20)
# this is how to draw bounding box
'''x1,y1 ------
    |          |
    |          |
    |          |
    --------x2,y2'''
# my_image=cv2.imread('american_bulldog_135.jpg',1)
my_image=cv2.imread('000010.png',1)
cv2.imshow('MyImage',my_image)
print(my_image.shape)
cv2.rectangle(my_image, pt1=top,pt2=bottom,color= (0,255,0), thickness=2)
cv2.rectangle(my_image, pt1=top1,pt2=bottom1,color= (0,255,0), thickness=2)
cv2.imshow('bounding_box image',my_image)
# '_______________________________________'
cv2.waitKey(0)
cv2.destroyAllWindows()