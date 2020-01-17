

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

detector = dlib.simple_object_detector("C:/Users/hichens/Desktop/detector1.svm")
cap = cv2.VideoCapture("D:Ubuntu/anydata/video/7.mp4")
out_video_path = "C:/Users/hichens/Desktop/zjc.mp4"

fps = 10
size = (544,960)

videoWriter = cv2.VideoWriter(out_video_path,cv2.VideoWriter_fourcc('I','4','2','0'),
                              fps,size)

n = 0
epson = 1 # 调整帧数的间隔

while (cap.isOpened()):
	ret, img = cap.read()

	if n % epson == 0:
		try:
			dets = detector(img)
		except:
			print("finished!")
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
		center_x = int(box_predict.left() + box_predict.right()) // 2
		center_y = int(box_predict.top() + box_predict.bottom()) // 2
		radiu = int(
			max(abs(box_predict.left() - box_predict.right()), abs(box_predict.top() - box_predict.bottom())) // 2)
		# print(center_x, center_y, radiu)
		cv2.circle(img, (center_x, center_y), radiu, (55, 255, 155), 3)
		#cv2.rectangle(img, (int(box_predict.left()), int(box_predict.top())),
		#			  (int(box_predict.right()), int(box_predict.bottom())), (93, 93, 223), 2)  # 用矩形框标注出来

	try:
		cv2.imshow("image", img)
		videoWriter.write(img)
	except:
		print("finished!")
		break
	# 如果按下ESC键，就退出
	if cv2.waitKey(10) == 27:
		break

cap.release()
cv2.destroyAllWindows()