from keras.models import model_from_json
from keras.preprocessing import image as im
from pathlib import Path

import cv2
import classifier

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0.
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, frame = self.video.read()
        
        if success:
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
            frame = classifier.classify(frame, self.face_detector, self.model)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()