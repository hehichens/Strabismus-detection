import cv2
import numpy as np
import dlib
from imageio import imread
import glob

'''

'''

def get_face_feature(img):
	detector = dlib.get_frontal_face_detector()
	dets = detector(img)
	print("检测到%d张人脸" % len(dets))
	for i, d in enumerate(dets):
		shape = predictor(img, d)

		landmarks = np.mat([[p.x, p.y] for p in shape.parts()])

		for idx, point in enumerate(landmarks):
			pos = (point[0, 0], point[0, 1])
			if 35 < idx < 48:
				cv2.putText(img, str(idx), pos, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
							fontScale=0.3, color=(0, 255, 0))  # 按照特征点的顺序加上数字，绿色点

		win.clear_overlay()
		win.set_image(img)  # 载入图片
		#win.add_overlay(shape)  # 特征点
	#win.add_overlay(dets) #外面的红框




cap = cv2.VideoCapture("D:/anydata/video/2.mp4") #0从摄像头读取视频，或者改成视频文件路径"D:/anydata/video/2.mp4"
win = dlib.image_window()

predictor_path = 'C:/Users/hichens/Desktop/Strabismus-detection/hichens/dat/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)

while(cap.isOpened()):
	ret, frame = cap.read()
	img = frame
	get_face_feature(img)

	k = cv2.waitKey(20)
	# q键退出
	if (k & 0xff == ord('q') or k & 0xff == ord('Q')):
		break

cap.release()
cv2.destroyAllWindows()