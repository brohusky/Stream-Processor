import cv2 as cv

from src.classifier import classifiers
from src.graphics import renderGraphics


class FrameProcessor:
    def mapClassifiers(self, frame, gray, overlay, classifier):
        detectedObjects = classifier.get('cascade').detectMultiScale(
            gray, scaleFactor=1.7, minNeighbors=5)

        for detectedObject in detectedObjects:
            renderGraphics(overlay, classifier, detectedObject)

        opacity = 0.4
        cv.addWeighted(overlay, opacity, frame, 1 - opacity, 0, frame)

    def process(self, frame):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        overlay = frame.copy()

        for classifier in classifiers:
            self.mapClassifiers(frame, gray, overlay, classifier)
