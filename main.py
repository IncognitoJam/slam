import cv2
import time
import sdl2
import sdl2.ext
import numpy as np
import skimage

from display import Display
from extractor import Extractor


size = (1920//2, 1080//2)
display = Display(size)
ex = Extractor()


def process_frame(img):
    img = cv2.resize(img, size)
    matches = ex.extract(img)

    print("%d matches" % (len(matches)))

    for pt1, pt2 in matches:
        u1, v1 = map(lambda x: int(round(x)), pt1)
        u2, v2 = map(lambda x: int(round(x)), pt2)
        cv2.circle(img, (u1, v1), color=(0, 255, 0), radius=3)
        cv2.line(img, (u1, v1), (u2, v2), (255, 0, 0))

    display.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("test.mkv")

    while cap.isOpened():
        display.poll()
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break
