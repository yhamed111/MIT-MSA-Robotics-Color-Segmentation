import cv2
import numpy as np
import imutils

# load in the image to be analyzed
original_img = cv2.imread("yellow_ball.jpg")

#### TODO ####
#### uncomment below and determine appropriate HSV value ranges for yellow ball
#### feel free to use a color picker online to help you with this

# H_min, H_max = 
# S_min, S_max =
# V_min, V_max =

##############

#### TODO ####
#### uncomment and complete the following lines to process the image for color
#### segmentation as discussed in lecture

#blurred_img = 
frame = cv2.cvtColor(blurred_img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(frame,(H_min , S_min , V_min),(H_max , S_max , V_max))
#erosion_mask = 
#dilation_mask = 

#### TODO ####
#### once the image has been blurred, eroded, and dilated, determine the color bounds
#### using the resulting dilation_mask array. HINT:the dilation_mask array is a 2D
#### array of 1's and 0's that represent where the the target color is found in the image
#### according to your chosen HSV ranges. Finally, use these bounds to draw a rectangular 
#### bounding box around the colored object in the original image (original_img)


cv2.imshow(original_img) ## original_img should have a bounding box in it once the code reaches this line

cv2.waitKey(0)
