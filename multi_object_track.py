import cv2
import numpy as np

# multi-object tracker
trackers = cv2.MultiTracker_create()

# web cam
vs = cv2.VideoCapture(0)

# loop
while True:
        ret, frame = vs.read()

        (success, boxes) = trackers.update(frame)

        for box in boxes:
                (x, y, w, h) = [int(v) for v in box]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the output
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # add tracker
        if key == ord("s"):
                trackers.clear()

                box = cv2.selectROI("Frame", frame, fromCenter=False,
                        showCrosshair=True)

                tracker = cv2.TrackerCSRT_create()
                trackers.add(tracker, frame, box)


        if key == ord("r"):
                """ remove trackers """

        # break
        elif key == ord("q"):
                break

vs.release()
cv2.destroyAllWindows()
