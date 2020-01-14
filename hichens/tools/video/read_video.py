import cv2
'''
读取视频
'''

'''
0:从摄像头读取
file_path
'''
cap = cv2.VideoCapture("D:/anydata/video/2.mp4")

while (cap.isOpened()):
	ret, frame = cap.read()
	cv2.imshow('image', frame)
	k = cv2.waitKey(20)
	# q键退出
	if (k & 0xff == ord('q') or k & 0xff == ord('Q')):
		break

cap.release()
cv2.destroyAllWindows()