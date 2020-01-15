# -*- coding: utf-8 -*-

import os
import sys
import dlib
import cv2
import glob

'''
从视频中追踪
训练好的 detector.svm 在 svm 文件中

'''
# "D:/anydata/video/8.mp4"
cap = cv2.VideoCapture(0)

detector = dlib.simple_object_detector("C:/Users/hichens/Desktop/Strabismus-detection/hichens/svm/detector.svm")
current_path = os.getcwd()
test_folder = "C:/Users/hichens/Desktop/Strabismus-detection/hichens/images/"
#win = dlib.image_window()

while (cap.isOpened()):
	ret, frame = cap.read()
	img = frame
	dets = detector(img)

	for index, face in enumerate(dets):
		print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
																	 face.bottom()))

		left = face.left()
		top = face.top()
		right = face.right()
		bottom = face.bottom()
		cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
		#cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
		cv2.imshow('eye', img)
	#cv2.imshow('image', frame)
	k = cv2.waitKey(20)
	# q键退出
	if (k & 0xff == ord('q') or k & 0xff == ord('Q')):
		break

cap.release()
cv2.destroyAllWindows()
