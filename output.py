import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
traffic_light_sequence={'Lane1':0,"Lane2":0,"Lane3":0,"Lane4":0}
#road1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fig=plt.figure(figsize=(2, 2), facecolor='w', edgecolor='k')
columns = 2
rows = 2
road4 = r'G:\python\car\4.jpg'   
road1 = r'G:\python\car\1.jpg'   
road2 = r'G:\python\car\2.JPG'   
road3 = r'G:\python\car\3.jpg'   
w=10
h=10
priority=1
# output_image1=cv2.imread(road1)
# output_image2=cv2.imread(road1)
# output_image3=cv2.imread(road1)
# output_image4=cv2.imread(road1)
output=['',cv2.imread(road1),cv2.imread(road1),cv2.imread(road1),cv2.imread(road1)]

time.sleep(2)
def getTrafficStatus():
    global priority
    road1Status=getRoad1()
    road2Status=getRoad2()
    road3Status=getRoad3()
    road4Status=getRoad4()
    traffic_light_sequence['Lane1']=road1Status
    traffic_light_sequence['Lane2']=road2Status
    traffic_light_sequence['Lane3']=road3Status
    traffic_light_sequence['Lane4']=road4Status
    print('\n')
    for i,j in sorted(traffic_light_sequence.items(), key=lambda item: item[1])[::-1]:
        print('priority {} '.format(priority),i,j)
        priority+=1
    for i in range(1, columns*rows +1):
        img = np.random.randint(10, size=(h,w))
        fig.add_subplot(rows, columns, i)
        plt.imshow(output[i])
    # fig.add_subplot(rows, columns, output_image1)
    # fig.add_subplot(rows, columns, output_image1)
    # fig.add_subplot(rows, columns, output_image1)
    # fig.add_subplot(rows, columns, output_image1)
    # plt.imshow(output_image1)
    # plt.show()
    # plt.imshow(output_image2)
    # plt.show()
    # plt.imshow(output_image3)
    # plt.show()
    # plt.imshow(output_image4)
    plt.show()
def getRoad1():
    global output_image1,output
    if( 1 ) :
        time.sleep(1)
        im = cv2.imread(road1)
        cv2.imshow("Lane1",im)
        k = cv2.waitKey(10)
        # bbox - box co-ordinates
        # label - object name
        # conf - confidence scores
        bbox, label, conf = cv.detect_common_objects(im)
        output[1] = draw_bbox(im, bbox, label, conf)
        print('\n')
        print('Lane 1 Status\n')
        print('Number of cars in the image is '+ str(label.count('car')))
        print('Number of bike in the image is '+ str(label.count('motorcycle')))
        print('Number of bus in the image is '+ str(label.count('bus')))
        print('Number of truck in the image is '+ str(label.count('truck')))
        
        return label.count('car')+label.count('motorcycle')+label.count('bus')+label.count('truck')
def getRoad2():
    global output_image2,output
    if( 1 ) :
        time.sleep(1)
        im = cv2.imread(road2)
        cv2.imshow("Lane2",im)
        k = cv2.waitKey(10)
        bbox, label, conf = cv.detect_common_objects(im)
        output[2] = draw_bbox(im, bbox, label, conf)
        print('\n')
        print('Lane 2 Status\n')
        print('Number of cars in the image is '+ str(label.count('car')))
        print('Number of bike in the image is '+ str(label.count('motorcycle')))
        print('Number of bus in the image is '+ str(label.count('bus')))
        print('Number of truck in the image is '+ str(label.count('truck')))

        return label.count('car')+label.count('motorcycle')+label.count('bus')+label.count('truck')
def getRoad3():
    global output_image3,output
    if( 1 ) :
        time.sleep(1)
        im = cv2.imread(road3)
        cv2.imshow("Lane3",im)
        k = cv2.waitKey(10)
        bbox, label, conf = cv.detect_common_objects(im)
        output[3] = draw_bbox(im, bbox, label, conf)
        print('\n')
        print('Lane 3 Status\n')
        print('Number of cars in the image is '+ str(label.count('car')))
        print('Number of bike in the image is '+ str(label.count('motorcycle')))
        print('Number of bus in the image is '+ str(label.count('bus')))
        print('Number of truck in the image is '+ str(label.count('truck')))

        return label.count('car')+label.count('motorcycle')+label.count('bus')+label.count('truck')
def getRoad4():
    global output_image4,output
    if( 1 ) :
        time.sleep(1)
        im = cv2.imread(road4)
        cv2.imshow("Lane4",im)
        k = cv2.waitKey(10)
        bbox, label, conf = cv.detect_common_objects(im)
        output[4] = draw_bbox(im, bbox, label, conf)
        print('\n')
        print('Lane 4 Status\n')
        print('Number of cars in the image is '+ str(label.count('car')))
        print('Number of bike in the image is '+ str(label.count('motorcycle')))
        print('Number of bus in the image is '+ str(label.count('bus')))
        print('Number of truck in the image is '+ str(label.count('truck')))
        return label.count('car')+label.count('motorcycle')+label.count('bus')+label.count('truck')
getTrafficStatus()

    
    