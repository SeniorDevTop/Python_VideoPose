import cv2
from ImagePose import *
import time

# initialize the video capture object
cap = cv2.VideoCapture('./video.mp4')

# check if the video capture object was successfully initialized
if not cap.isOpened():
    print('Error: Could not open video.')
    exit()


while True:
    # read a frame from the video
    ret, frame = cap.read()

    strSaveImgPath = "./img.jpg"
    # print(frame)
    # break
    # image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame)
    pil_image.save(strSaveImgPath)

    annotated_image, visualized_mask = imgPose(imgPath=strSaveImgPath)


    # check if the frame was successfully read
    if not ret:
        print('Error: Could not read frame.')
        break

    # cv2.namedWindow('My Window', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('My Window', 300, 200)
    # display the frame
    cv2.imshow('image', annotated_image)
    # cv2.imshow('Frame', frame)

    # wait for 25 milliseconds
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    time.sleep(0.1)

# release the resources used by the video capture object
cap.release()

# destroy all windows created by OpenCV
cv2.destroyAllWindows()
