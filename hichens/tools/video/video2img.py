'''
将video转换成images

关键参数
videoFile 视频输出路径
outputFile 图片路径
timeF ：帧数间隔
'''

import cv2
videoFile = 'D:/anydata/video/4.mp4'
outputFile = 'D:/anydata/images/'

vc = cv2.VideoCapture(videoFile)
c = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    print('openerror!')
    rval = False

timeF = 10  #视频帧计数间隔次数
while rval:
    print(1)
    #print(c)
    rval, frame = vc.read()
    if c % timeF == 0:
        print(2)
        cv2.imwrite(outputFile + str(int(c / timeF)) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
vc.release()
