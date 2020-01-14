import os
import cv2


'''
这个工具用来从多个视频中获取图片
得到图片用来打标
'''
path = 'D:/anydata/video'

outputFile = 'D:/anydata/images/'


index = 1
for i in range(1, 5):

	videoFile = os.path.join(path, str(i)+'.mp4')
	vc = cv2.VideoCapture(videoFile)

	if vc.isOpened():
		rval, frame = vc.read()
	else:
		print('openerror!')
		rval = False

	timeF = 1000  #视频帧计数间隔次数
	while rval:
		rval, frame = vc.read()
		cv2.imwrite(outputFile + str(index // 10) + '.jpg', frame)
		index += 1
		cv2.waitKey(1)
	print(i)
	vc.release()
