import cv2 as cv

from random import randint

faceCascade = cv.CascadeClassifier('./classifiers/haarcascades/haarcascade_frontalface_default.xml')
eyeCascade = cv.CascadeClassifier('./classifiers/haarcascades/haarcascade_eye.xml')

opacity = 0.4

rectangleColor = ()

class FrameProcessor:
  def process(self, frame):
    overlay = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
      cv.rectangle(\
        overlay,\
        (x, y),\
        (x + w, y + h),\
        self._getRectangleColor(),\
        10\
      )

    cv.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)

  def _getRectangleColor(self):
    color = randint(100, 150)
    return (color, color, color)