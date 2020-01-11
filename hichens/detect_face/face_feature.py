'''
得到人脸的特征

关键参数
predictor_path: dat文件
path: 图片路径

'''

import numpy as np
import dlib
import cv2
from imageio import imread
import glob

detector = dlib.get_frontal_face_detector()
win = dlib.image_window()

predictor_path = 'dat/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)

path = "images/13.jpg"
img = imread(path)
dets = detector(img) #dets为检测到的人脸对象
print('检测到了 %d 个人脸' % len(dets))

for i, d in enumerate(dets):
	print('- %d: Left %d Top %d Right %d Bottom %d' % (i, d.left(), d.top(), d.right(), d.bottom()))
	shape = predictor(img, d)
	landmarks = np.mat([[p.x, p.y] for p in shape.parts()])
	print("\n".format(landmarks))
	'''
	获取每个关键点坐标shape.parts()的x,y值，
	存入landmark矩阵（模型默认提取68个关键点，所以landmark为68×2矩阵）
	'''
	# 第 0 个点和第 1 个点的坐标
	print('Part 0: {}, Part 1: {}'.format(shape.part(0), shape.part(1)))
	for idx, point in enumerate(landmarks):
		pos = (point[0, 0], point[0, 1])
		cv2.putText(img, str(idx), pos, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
				fontScale=0.3, color=(0, 255, 0)) # 按照特征点的顺序加上数字

win.clear_overlay()
win.set_image(img)#载入图片
#win.add_overlay(dets) #外面的红框
win.add_overlay(shape) #特征点

dlib.hit_enter_to_continue() #用于等待点击（类似于opencv的cv2.waitKey(0)，不加这个会出现闪退