# Python code for Background subtraction using OpenCV
import numpy as np
import cv2

#########################################  INITIAL VARIABLE   ####################################
sx = 0
sy = 0
ex = 799
ey = 599
total_num = 0
fsz = 500

#########################################  CREATE BACKGROUND SUBSTRACTOR  ####################################

fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=100)
frame = cv2.imread("1.jpg")
w, h = frame.shape[:2]

froi = frame[sy:ey, sx:ex]
fgmask = fgbg.apply(froi)
cv2.waitKey(10)


#########################################  OPEN NEW IMAGE & DETECT FISH REGION  ####################################

frame = cv2.imread("4.jpg")
eroi = frame[sy:ey, sx:ex]
fgmask = fgbg.apply(eroi)


#########################################  CONTOUR AND AREA CALCULATION  ####################################
cv2.imshow("window1", froi)
cv2.imshow("window2", eroi)

kernel = np.ones((9, 9), np.uint8)
thres_img = cv2.erode(fgmask, kernel)

contours, _ = cv2.findContours(thres_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
	area = cv2.contourArea(cnt)
	x,y,w,h = cv2.boundingRect(cnt)
	
	if area > fsz and w * h < area * 4:
		cv2.drawContours(eroi, [cnt], -1, (0, 255, 0), 1)
		
		total_num = total_num + 1


print("Total Fish Count: ", total_num)
cv2.imshow("window", eroi)
cv2.waitKey(0)
cv2.destroyAllWindows()

