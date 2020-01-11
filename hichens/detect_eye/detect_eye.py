import dlib
import numpy
import sys
import os
from math import *
import cv2


# 获取原始图片
def getAllImg(folder):
	assert os.path.exists(folder)
	assert os.path.isdir(folder)
	imgList = os.listdir(folder)
	imgList = [item for item in imgList if os.path.isfile(os.path.join(folder, item))]
	return imgList


imgList = getAllImg('./images')
# print(imgList)  # 打印所有的图片名
PREDICTOR_PATH = 'D:/anydata/shape_predictor_68_face_landmarks.dat'  # 关键点提取模型路径
landmarks = []  # 存储人脸关键点
# 1. 定义人脸检测器
detector = dlib.get_frontal_face_detector()

# 2. 载入关键点提取模型
predictor = dlib.shape_predictor(PREDICTOR_PATH)
have_face_img_num = 0  # 统计检测到人脸的图片个数

print('*** Face detection start! ***')


def get_fea_points(rects, im, new_name):
	global landmarks
	feas = []  # 关键点
	fea_file_name = new_name[:-3] + 'pts'  # pts文件名为旋转后图片名称.pts
	fea_file = open('./images/' + fea_file_name, 'a')  # 新建pts文件
	fea_file.write('version: 1' + '\n' + 'n_points: 68' + '\n' + '{' + '\n')  # 写入文件头部信息
	for i in range(len(rects)):  # 遍历所有检测到的人脸（我的是单个人脸）
		landmarks = numpy.matrix([[p.x, p.y] for p in predictor(im, rects[i]).parts()])
	# print(landmarks)
	im_circle = im.copy()
	im_text = im.copy()
	# 使用enumerate 函数遍历序列中的元素以及它们的下标
	for idx, point in enumerate(landmarks):
		pos = (point[0, 0], point[0, 1])  # 依次保存每个关键点
		feas.append(pos)
		# 在图上画出关键点
		cv2.putText(im_text, str(idx), pos, fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=0.3, color=(0, 255, 0))
		cv2.circle(im_circle, pos, 2, color=(0, 0, 255))

	for pos in feas:
		fea_file.write(str(pos[0]) + ' ' + str(pos[1]) + '\n')  # 写如特征点到pts文件
	fea_file.write('}')  # 写pts文件尾部
	fea_file.close()
	# cv2.namedWindow("im", 2)  # 显示标记特征点的图片
	# cv2.imshow("im", im)
	# cv2.waitKey(0)
	return im_circle, im_text, feas


img_name = 'm9.jpg'
im = cv2.imread('./images/' + img_name)
rotate_num = 0  # 旋转的次数
degree = 60  # 每次旋转的角度

while 1:
	rotate_num += 1
	rects = detector(im, 1)  # 检测人脸
	if len(rects) >= 1:  # 检测到人脸
		have_face_img_num += 1
		print('img {}: rotating {} degree, get {} faces detected!'.format(img_name, degree * (rotate_num - 1),
																		  len(rects)))
		row, col = im.shape[:2]
		# if row > 600 and col > 600:  # 如果图片太大，从中心位置取600×600的切片
		# im = im[row / 2 - 300:row / 2 + 300, col / 2 - 300:col / 2 + 300, :]
		rects = detector(im, 1)  # 再次检测人脸框，一般还是可以检测到的，所以这里没判断
		new_name = img_name.split('.')[0] + '_' + str(
			degree * (rotate_num - 1)) + '.png'  # 重新命名图片，命名规则为原来的图片名+旋转角度
		(im_circle, im_text, feas) = get_fea_points(rects, im, new_name)  # 调用关键点子程序，见步骤d）
		name_c = new_name.split('.')[0] + '_c' + '.png'
		name_t = new_name.split('.')[0] + '_t' + '.png'
		name_l = new_name.split('.')[0] + '_l' + '.png'
		name_e = new_name.split('.')[0] + '_e' + '.png'
		cv2.imwrite('./images/' + name_c, im_circle)  # 保存图片到新的文件夹
		cv2.imwrite('./images/' + name_t, im_text)  # 保存图片到新的文件夹

		feas1 = numpy.array([[feas[i] for i in range(0, 17)]])  # 脸
		feas2 = numpy.array([[feas[i] for i in range(17, 22)]])  # 左眼眉
		feas3 = numpy.array([[feas[i] for i in range(22, 27)]])  # 右眼眉
		feas4_1 = numpy.array([[feas[i] for i in range(27, 31)]])  # 鼻子1
		feas4_2 = numpy.array([[feas[i] for i in range(30, 36)]])  # 鼻子2
		feas5 = numpy.array([[feas[i] for i in range(36, 42)]])  # 左眼
		feas6 = numpy.array([[feas[i] for i in range(42, 48)]])  # 右眼
		feas7 = numpy.array([[feas[i] for i in range(48, 60)]])  # 外嘴唇
		feas8 = numpy.array([[feas[i] for i in range(60, 68)]])  # 内嘴唇

		im_line = im.copy()
		num = 1
		color = (0, 0, 0)
		cv2.polylines(im_line, feas1, False, color, num)
		cv2.polylines(im_line, feas2, False, color, num)
		cv2.polylines(im_line, feas3, False, color, num)
		cv2.polylines(im_line, feas4_1, True, color, num)
		cv2.polylines(im_line, feas4_2, True, color, num)
		cv2.polylines(im_line, feas5, True, color, num)
		cv2.polylines(im_line, feas6, True, color, num)
		cv2.polylines(im_line, feas7, True, color, num)
		cv2.polylines(im_line, feas8, True, color, num)

		im_eye = im.copy()
		cv2.polylines(im_eye, feas5, True, (0, 255, 0), num)
		cv2.polylines(im_eye, feas6, True, (0, 255, 0), num)

		# cv2.drawContours(im_line,feas1,-1,(255,0,0),1)
		cv2.imwrite('./images/' + name_l, im_line)
		cv2.imwrite('./images/' + name_e, im_eye)
		break
	else:  # 如果检测不到人脸
		if rotate_num == int(360 / degree):  # 判断是否旋转完360度
			print(
				'img {}: after rotate {} degree, No face is detected!'.format(img_name, degree * (rotate_num - 1)))
			break
		# 旋转60度
		rows, cols, channel = im.shape
		# 为了旋转之后不裁剪原图，计算旋转后的尺寸
		rowsNew = int(cols * fabs(sin(radians(degree))) + rows * fabs(cos(radians(degree))))
		colsNew = int(rows * fabs(sin(radians(degree))) + cols * fabs(cos(radians(degree))))
		M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)  # 旋转60度的仿射矩阵
		M[0, 2] += (colsNew - cols) / 2
		M[1, 2] += (rowsNew - rows) / 2
		im = cv2.warpAffine(im, M, (colsNew, rowsNew), borderValue=(255, 255, 255))  # 旋转60度，得到新图片

print('*** success: {} / {}  ***'.format(have_face_img_num, len(imgList)))