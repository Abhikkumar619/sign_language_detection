import os
import cv2
import time 
import uuid # display string of haxadecimal digits and seprate by hyphens.

IMAGE_PATH='CollectedImages'
labels=['Hello', 'Yes', 'No', 'Thanks','IloveYou', 'Please']

number_of_images=20

for label in labels:    
    # creating directory for Image.
    img_path=os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path)

    #initializes a video capture object in Opencv to capture video from default camera of computer.
    cap=cv2.VideoCapture(0)
    print('Collection images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_of_images):

        # After creating the videocapture read() to capture frames from camera.
        # ret() is a boolean indicating whether the frame was read successfully.
        ret, frame=cap.read()
        #UUID: universally unique identifier based on the host mac address and current timestamp. 
        # display string of haxadecimal digits and seprate by hyphens.
        imagename=os.path.join(IMAGE_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        # save the image to file system.
        cv2.imwrite(imagename, frame)
        # Display the image in a windows titled 'frame'.
        cv2.imshow('frame',frame)
        time.sleep(2)

        #  Break out of a loop when q key is pressed.
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    # close the camera when program finish using them.
    cap.release()