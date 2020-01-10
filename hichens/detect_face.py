import cv2
import  dlib

detector = dlib.get_frontal_face_detector()

'''
0:从摄像头读取
file_path
'''
cap = cv2.VideoCapture(0)
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