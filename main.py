import os
import cv2 as cv

faceCascade = cv.CascadeClassifier('./classifiers/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv.CascadeClassifier('./classifiers/haarcascades/haarcascade_eye.xml')

opacity = 0.4

class FaceDetector:
  def __init__(self):
    self.cap = cv.VideoCapture(0)

  def detection(self, frame):
    overlay = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
      cv.rectangle(\
        overlay,\
        (x, y),\
        (x + w, y + h),\
        (255, 255, 255),\
        5\
      )

    cv.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)
 

  def process(self):
    ret, frame = self.cap.read()

    self.detection(frame)

    self.monitor(frame)

  # Show Window frame for monitoring
  def monitor(self, frame):
    if os.getenv('ENV') == 'development':
      cv.namedWindow('Live Feed!')
      cv.imshow('Live Feed!', frame)

  # Process tear down
  def release(self):
    self.cap.release()
    cv.destroyAllWindows()

  # Bootstrap
  def launch(self):
    while True:
      self.process()
      if cv.waitKey(20) & 0xFF == ord('q'):
        break
    self.release()

if __name__ == "__main__":
  faceDetector = FaceDetector()
  faceDetector.launch()
