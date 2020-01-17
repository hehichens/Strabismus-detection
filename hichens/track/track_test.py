# -*- coding: utf-8 -*-

import os
import sys
import dlib
import cv2
import glob
'''
用来测试
我用的是images文件中的图片
每个都找的很准确！
训练好的 detector.svm 在 svm 文件中

'''
detector = dlib.simple_object_detector("detector1.svm")

current_path = os.getcwd()
test_folder = "C:/Users/hichens/Desktop/Strabismus-detection/hichens/images/"

for f in glob.glob(test_folder+'*.jpg'):
    print("Processing file: {}".format(f))
    img = cv2.imread(f, cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    dets = detector(img2)
    print("Number of faces detected: {}".format(len(dets)))
    for index, face in enumerate(dets):
        print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(), face.bottom()))

        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
        cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
        cv2.imshow(f, img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()