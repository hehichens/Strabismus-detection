

import sys
import dlib
import cv2

'''
雏形的识别加跟踪算法，检测并追踪瞳孔。

调试参数epson即可，epson为帧间隔数
'''

track = [] #track分别跟踪左右眼
for i in range(2):
	track.append(dlib.correlation_tracker())

detector = dlib.simple_object_detector("/home/hichens/Desktop/detector1.svm")
cap = cv2.VideoCapture("/mnt/hgfs/Ubuntu/anydata/video/7.mp4")

def detector_img(img):
	try:
		dets = detector(img) #第一次检测到的两个瞳孔
	except:
		print("finished")
		sys.exit(0)

	for i, eye in enumerate(dets):
		print('eye {}; left {}; top {}; right {}; bottom {}'.format(i, eye.left(), eye.top(), eye.right(),
																	eye.bottom()))

		left = eye.left()
		top = eye.top()
		right = eye.right()
		bottom = eye.bottom()

		cv2.rectangle(img, (left, top), (right, bottom), (93, 93, 223), 2)
		cv2.imshow('eye', img)


n = 0
epson = 6 # 调整帧数的间隔

while (cap.isOpened()):
	ret, frame = cap.read()
	img = frame

	if n % epson == 0:
		dets = detector(img)
		#flag = False
		for i, eye in enumerate(dets):
			left = eye.left()
			top = eye.top()
			right = eye.right()
			bottom = eye.bottom()

			#控制最多检测数两个瞳孔
			if i >=2:
				break

			track[i].start_track(img, dlib.rectangle(left, top, right, bottom))
	n += 1
	for i in range(2):
		box_predict = track[i].get_position()  # 得到目标的位置
		cv2.rectangle(img, (int(box_predict.left()), int(box_predict.top())),
					  (int(box_predict.right()), int(box_predict.bottom())), (93, 93, 223), 2)  # 用矩形框标注出来

	try:
		cv2.imshow("image", frame)
	except:
		print("finished!")
		break
	# 如果按下ESC键，就退出
	if cv2.waitKey(10) == 27:
		break

cap.release()
cv2.destroyAllWindows()