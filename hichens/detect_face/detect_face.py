'''
从视频里面识别人脸

改变VideoCapture参数
(1).0:从摄像头读取
(2). file_path
'''

import cv2
import  dlib

detector = dlib.get_frontal_face_detector()

'''

'''
cap = cv2.VideoCapture("D:/anydata/video/8.mp4") #0从摄像头读取视频，或者改成视频文件路径
win = dlib.image_window()

while (cap.isOpened()):
	ret, frame = cap.read()
	img = frame
	dets = detector(img)
	win.clear_overlay()
	win.set_image(img)
	win.add_overlay(dets)
	k = cv2.waitKey(20)
	# q键退出

	if (k & 0xff == ord('q') or k & 0xff == ord('Q')):
		break

cap.release()
cv2.destroyAllWindows()