import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
traffic_light_other={'Road1':0,"Road2":0,"Road3":0,"Road4":0}
road1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# road2 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# road3 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# road4 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(2)
def getTrafficStatus():
    road1Status=getRoad1()
    # road2Status=getRoad2()
    # road3Status=getRoad3()
    # road4Status=getRoad4()
    traffic_light_other['Road1']=road1Status
    # traffic_light_other['Road2']=road2Status
    # traffic_light_other['Road3']=road3Status
    # traffic_light_other['Road4']=road4Status
    for i,j in sorted(traffic_light_other.items(), key=lambda item: item[1])[::-1]:
        print(i,j)
def getRoad1():
    if( road1.isOpened() ) :
        time.sleep(1)
        _,im = road1.read()
        cv2.imshow("lll",im)
        k = cv2.waitKey(10)
        # if k == 27:
        #     break
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)
        print('Number of cars in the image is '+ str(label.count('car')))
        print('Number of bike in the image is '+ str(label.count('motorcycle')))
        print('Number of bus in the image is '+ str(label.count('bus')))
        print('Number of truck in the image is '+ str(label.count('truck')))
       
        plt.imshow(output_image)
        plt.show()
        return label.count('car')+label.count('motorcycle')+label.count('bus')+label.count('truck')
getTrafficStatus()

    
    