import cv2 as cv

font      = cv.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
fontColor = (255,255,255)
thickness = 2

def renderGraphics(overlay, classifier, detectedObject):
    (x, y, w, h) = detectedObject
    # Rectangle
    cv.rectangle(\
      overlay,\
      (x, y),\
      (x + w, y + h),\
      classifier.get('color'),\
      1\
    )
    
    # Text
    (textWidth, textHeight) = cv.getTextSize(classifier.get('text'), font, fontScale, thickness)[0]
    cv.rectangle(\
      overlay,\
      (x, y + h),\
      (x + textWidth + 10, y + h + textHeight + 10),\
      classifier.get('color'),\
      cv.FILLED \
    )
    cv.putText(overlay, classifier.get('text'), (x + 5, y + h + textHeight + 5), font, fontScale, classifier.get('textColor'), thickness)
