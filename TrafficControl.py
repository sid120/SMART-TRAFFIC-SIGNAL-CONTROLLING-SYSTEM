import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt
import time as t


im = cv2.imread('ROAD-ARTICLE2.jpg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()

im1 = cv2.imread('IndiaTraffic.jpg')
bbox1, label1, conf1 = cv.detect_common_objects(im1)
output_image1 = draw_bbox(im1, bbox1, label1, conf1)
plt.imshow(output_image1)
plt.show()


a = int(str(label.count('car')))
b = int(str(label.count('person')))
c = int(str(label.count('motorcycle')))
d = int(str(label.count('truck')))
j = int(str(label.count('bus')))


e = int(str(label1.count('car')))
f = int(str(label1.count('person')))
g = int(str(label1.count('bus')))
h = int(str(label1.count('truck')))
i = int(str(label.count('motorcycle')))

sum1 = a+b+c+d+j
sum2 = e+f+g+h+i

if sum1 > sum2:
    print("Green for Side1")
    print("Red for Side2 for +20s")

else:
    print("Green for Side2")
    print("Red for Side1 for +20s")

