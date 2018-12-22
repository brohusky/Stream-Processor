import cv2 as cv

from PIL import ImageFont

font = cv.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
thickness = 2
textPadding = 10


def renderGraphics(overlay, classifier, detectedObject):
    (x, y, w, h) = detectedObject
    # Rectangle
    cv.rectangle(
        overlay,
        (x, y),
        (x + w, y + h),
        classifier.get('color'),
        1
    )

    # Text
    (textWidth, textHeight) = cv.getTextSize(
        classifier.get('text'), font, fontScale, thickness)[0]
    cv.rectangle(
        overlay,
        (x, y + h),
        (x + textWidth + textPadding, y + h + textHeight + textPadding),
        classifier.get('color'),
        cv.FILLED
    )
    cv.putText(overlay, classifier.get('text'), (x + (textPadding // 2), y + h + textHeight +
                                                 (textPadding // 2)), font, fontScale, classifier.get('textColor'), thickness)
