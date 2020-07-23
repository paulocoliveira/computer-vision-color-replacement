import cv2
import numpy as np
import time

#capture video
video = cv2.VideoCapture("chroma.mp4")

while video:
    #load the image to substitute the background
    background = cv2.imread("background.jpg")

    #capture a frame
    video_return, frame = video.read()

    #verify video status
    if not video_return:
        exit()
    
    #redize the background image to the same size of the video
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    #lower and upper limits of the desired color (green)
    lower_range = np.array([0,150,0], dtype=np.uint8)
    upper_range = np.array([100,255,100], dtype=np.uint8)

    #create a mask using ranges
    mask = cv2.inRange(frame, lower_range, upper_range)

    #process the background using the mask, removing things in common with the black area
    background_process = cv2.bitwise_and(background, background, mask = mask)

    #invert mask colors to invert selection
    invert_mask = np.invert(mask)

    #process the frame using the mask, removing things in common with the white area
    frame_process = cv2.bitwise_and(frame, frame, mask = invert_mask)

    #unify video and image
    final = cv2.addWeighted(background_process,1,frame_process,1,0)

    #show the video with image background
    cv2.imshow("mask", final)

    #wait until a key is pressed
    c = cv2.waitKey(5)

    if c == ord("q"):
        break

cv2.destroyAllWindows

    


    
    
