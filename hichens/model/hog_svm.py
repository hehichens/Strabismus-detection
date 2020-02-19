

import sys
import dlib
import cv2

'''
基于HOG+SVM的
雏形的识别加跟踪算法，检测并追踪瞳孔
调试参数epson即可，epson为帧间隔数
测试环境：Ubuntu 18.1
'''

track = [] #track分别跟踪左右眼
for i in range(2):
	track.append(dlib.correlation_tracker())

detector = dlib.simple_object_detector("/mnt/hgfs/Ubuntu/Strabismus-detection/hichens/svm/detector.svm")#加载SVM文件
cap = cv2.VideoCapture("/mnt/hgfs/Ubuntu/anydata/video/me4.mp4")# 0打开摄像头"/mnt/hgfs/Ubuntu/anydata/video/12.mp4"
out_video_path = "/mnt/hgfs/Ubuntu/anydata/video/hc.avi"#保存位置

fps = 30 # 每秒的帧数
size = (int(cap.get(3)), int(cap.get(4))) # size 注意顺序的是宽高
fourcc = cv2.VideoWriter_fourcc(*'XVID') # FourCC是一个4字节代码，用于指定视频编解码器
videoWriter = cv2.VideoWriter(out_video_path, fourcc, fps, size)

n = 0 # 控制间隔
epson = 1 # 调整帧数的间隔

while (cap.isOpened()):
	ret, img = cap.read()
	# ret:bool型
	if not ret:
		print("Finished!")
		break

	if n % epson == 0:
		dets = detector(img)
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

	cv2.imshow("image", img)
	videoWriter.write(img)
	# 如果按下ESC键，就退出
	if cv2.waitKey(10) == 27:
		break

cap.release()
cv2.destroyAllWindows()

'''
测试结果：
	1.epson等于６的时候几乎可以满足实时跟踪，但是效果很差
	2.对于医生给的视频效果还可以
	3.自己拍的视频效果不行,原因暂时未知，估计可能是距离的原因
	4.戴眼镜效果会变差
	5.光线弱环境下效果差
'''