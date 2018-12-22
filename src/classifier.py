import cv2 as cv

classifiers = [
  {
    'text': 'Face',
    'cascade': cv.CascadeClassifier('classifiers/haarcascades/haarcascade_frontalface_default.xml'),
    'color': (0, 0, 255),
    'textColor': (255, 255, 255)
  },
  {
    'text': 'Face',
    'cascade': cv.CascadeClassifier('classifiers/haarcascades/haarcascade_profileface.xml'),
    'color': (0, 0, 255),
    'textColor': (255, 255, 255)
  },
  {
    'text': 'Full Body',
    'cascade': cv.CascadeClassifier('classifiers/haarcascades/haarcascade_fullbody.xml'),
    'color': (255, 0, 0),
    'textColor': (255, 255, 255)
  }
]
