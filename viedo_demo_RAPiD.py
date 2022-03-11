import cv2
import imutils
from api import Detector
from PIL import Image
import os

# Initialize detector
detector = Detector(model_name='rapid',
                    weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                    use_cuda=True)

cap = cv2.VideoCapture('D01_20220125172918.mp4')

frameCount=0
numFrames2Skip=5000

while cap.isOpened():
    # Reading the video stream
    ret, image = cap.read()
    if ret:
        frameCount+=1
        if frameCount<numFrames2Skip:
            continue
        image = imutils.resize(image,width=min(400, image.shape[1]))
        # Detecting all the regions in the Image that has a pedestrians inside it
        image = detector.detect_one_frame(img=image, return_img=True,
                                    input_size=1024, conf_thres=0.4, test_aug=None, )
        # os.remove('temp.jpg')
        cv2.imshow("Pedestrian Tracking", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()
