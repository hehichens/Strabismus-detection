# -*- coding: utf-8 -*-
import os
import sys
import glob
import dlib
import cv2
'''
用来训练

训练集和测试集的train.xml和test.xml在xml文件中

detector.svm为输出的文件
'''
# options用于设置训练的参数和模式
options = dlib.simple_object_detector_training_options()
# Since faces are left/right symmetric we can tell the trainer to train a
# symmetric detector.  This helps it get the most value out of the training
# data.
options.add_left_right_image_flips = True
# 支持向量机的C参数，通常默认取为5.自己适当更改参数以达到最好的效果
options.C = 5
# 线程数，你电脑有4核的话就填4
options.num_threads = 4
options.be_verbose = True

# 获取路径
path = "C:/Users/hichens/Desktop"
train_xml_path = "D:/Ubuntu/images/images_train/xml_train.xml"
test_xml_path  = "D:/Ubuntu/images/images_test/xml_test.xml"

#out_path = "C:/Users/hichens/Desktop/detector.svm"

print("training file path:" + train_xml_path)
# print(train_xml_path)
print("testing file path:" + test_xml_path)
# print(test_xml_path)

# 开始训练
print("start training:")
dlib.train_simple_object_detector(train_xml_path, 'detector1.svm', options)

print("")  # Print blank line to create gap from previous output
print("Training accuracy: {}".format(
    dlib.test_simple_object_detector(train_xml_path, "detector1.svm")))

print("Testing accuracy: {}".format(
    dlib.test_simple_object_detector(test_xml_path, "detector1.svm")))