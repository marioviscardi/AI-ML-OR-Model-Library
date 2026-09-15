import cv2
import numpy as np

cap = cv2.VideoCapture(0)

for i in range(10):
    success, old_frame = cap.read()
if not success:
    exit(1)

old_gray_frame = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
old_points = cv2.goodFeaturesToTrack(
    old_gray_frame, maxCorners=100, qualityLevel=0.3, minDistance=7,
    blockSize=7)

term_crit = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 0.03)
overlay = np.zeros_like(old_frame)
colors = np.random.randint(0, 255, (100, 3))

success, frame = cap.read()
while(success):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    points, statuses, distances = cv2.calcOpticalFlowPyrLK(
         old_gray_frame, gray_frame, old_points, None,
         winSize=(15, 15), maxLevel=2, criteria=term_crit)

    good_points = points[statuses==1]
    good_old_points = old_points[statuses==1]

    for i, (point, old_point) in enumerate(zip(good_points, good_old_points)):
        a, b = point.ravel()
        c, d = old_point.ravel()
        a, b, c, d = int(a), int(b), int(c), int(d)
        color = colors[i].tolist()
        cv2.line(overlay, (a, b), (c, d), color, 2)
        cv2.circle(frame, (a, b), 5, color, cv2.FILLED)
    cv2.add(frame, overlay, frame)
    cv2.imshow('lk', frame)

    k = cv2.waitKey(1)
    if k == 27:
        break

    old_gray_frame = gray_frame
    old_points = good_points.reshape(-1, 1, 2)
    success, frame = cap.read()

cv2.destroyAllWindows()
cap.release()
