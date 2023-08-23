import cv2
import numpy as np
import imutils


def nothing(val):
    pass
cv2.namedWindow('W')
cv2.createTrackbar("H_min", "W", 0, 255, nothing)#, hue_min_callback)
cv2.createTrackbar("H_max", "W", 0, 255, nothing)#, hue_max_callback)
cv2.createTrackbar("S_min", "W", 0, 255, nothing)#, sat_min_callback)
cv2.createTrackbar("S_max", "W", 0, 255, nothing)#, sat_max_callback)
cv2.createTrackbar("V_min", "W", 0, 255, nothing)#, value_min_callback)
cv2.createTrackbar("V_max", "W", 0, 255, nothing)#, value_max_callback)


vid = cv2.VideoCapture(0)
while True:
    H_min, H_max = cv2.getTrackbarPos("H_min", "W"), cv2.getTrackbarPos("H_max", "W")   #0, 10
    S_min, S_max = cv2.getTrackbarPos("S_min", "W"), cv2.getTrackbarPos("S_max", "W")   #100, 255
    V_min, V_max = cv2.getTrackbarPos("V_min", "W"), cv2.getTrackbarPos("V_max", "W")   #20, 255

    ret, original_img = vid.read()

    #### TODO ####
    #### take your code from color_segmentation_still.py, and paste and modify it below so that
    #### it continuously runs the color segmentation on frames from your webcam.
    #### take a monochromatic object laying around, and test it, using the provided HSV sliders
    #### to adjust the HSV ranges appropriately and easily!
     
    #PASTE HERE

    #### 

    cv2.imshow("color segmentation", original_img)

    if cv2.waitKey(1) & 0xFF == ord('q'): #### press q to quit the application
        break

vid.release()
cv2.destroyAllWindows()