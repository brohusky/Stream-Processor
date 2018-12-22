import os
import cv2 as cv

from frame_processor import FrameProcessor

class FaceDetector:
  def __init__(self):
    self.cap = cv.VideoCapture(0)
    self.frameProcessor = FrameProcessor()

  def process(self):
    ret, frame = self.cap.read()

    # process pipeline
    self.frameProcessor.process(frame)
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
