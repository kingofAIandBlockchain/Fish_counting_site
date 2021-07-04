###########################
#   Date: 2021/07/04      #
#                         #
###########################

from django.conf import settings


import cv2 as cv
import numpy as np
import random
import os


def counting(file_names):
    
    ### Split Input String ###
    fn_array = file_names.split("`")
    ### KNN Background Substraction ####
    bgs = cv.createBackgroundSubtractorKNN(dist2Threshold=500,detectShadows=False)

    ### Count AVG Number ### 
    avg = 0    
    ### Get a length ###
    ln = len(fn_array)
    last_path = "." + settings.MEDIA_URL + fn_array[ln - 1]
    ### Loop Filenames ###
    for i in range(ln - 1):

        ### Initialize Count Number Every Loop ###
        cnt = 0
        
        path1 = "." + settings.MEDIA_URL + fn_array[i]
        path2 = "." + settings.MEDIA_URL + fn_array[i + 1]
        ### Open Currnet Image And Next Image ###
        frame1 = cv.imread(path1, 1)
        frame2 = cv.imread(path2, 1)
        print("@@@@", path1, "@@", path2)

        if frame1 is None or frame2 is None:
            return "Please check image path"

        ### Get A Size of Image(h: height, w: weight) ###
        h, w = frame1.shape[:2]
        
        ### Calculate Rate on 300px(width) ### 
        rx = w / 300
        h = int(h / rx)

        ### Resize Image ###
        frame1 = cv.resize(frame1, (300, h))
        frame2 = cv.resize(frame2, (300, h))
        h, w = frame1.shape[:2]
        
        ### Convert Color for processing ###
        gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
        gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    
        dif_img = cv.absdiff(gray1, gray2)
        _, th_img = cv.threshold(dif_img, 10, 255, cv.THRESH_BINARY)

        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(9, 9))
        th_img = cv.erode(th_img, kernel)

        kernel = cv.getStructuringElement(cv.MORPH_RECT,(35, 35))
        th_img = cv.dilate(th_img, kernel)

        
        contours, hie = cv.findContours(th_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        

        for contour in contours:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            area = cv.contourArea(contour)
            if(area > (h * w * 0.01)):
                cv.drawContours(frame2, [contour], -1, (r,g,b), -1)
                cnt += 1
        
            
        avg += cnt;
        os.remove(path1)
        # cv.imshow("Frame2", frame2)
        # cv.imshow("Threshold", th_img)
        # cv.waitKey(0)
    
    
    os.remove(last_path)
    avg = int((avg / ln) + 0.5)
    return str(avg)
        