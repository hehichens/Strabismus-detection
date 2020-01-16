# @hichens

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


class Hog_descriptor():
    def __init__(self, img, cell_size=16, bin_size=8):
        self.img = img
        '''
        伽马校正
        self.img = np.sqrt(img / np.max(img))
        self.img = img * 255
        '''
        self.cell_size = cell_size
        self.bin_size = bin_size
        self.angle_unit = 360 / self.bin_size

    def extract(self):
        height, width = self.img.shape
        #1.计算每个像素的梯度和方向
        gradient_magnitude, gradient_angle = self.global_gradient()
        gradient_magnitude = abs(gradient_magnitude)

        cell_gradient_vector = np.zeros((height // self.cell_size, width // self.cell_size, self.bin_size))
        for i in range(cell_gradient_vector.shape[0]):
            for j in range(cell_gradient_vector.shape[1]):
                #取一个cell中的梯度大小和方向
                cell_magnitude = gradient_magnitude[i * self.cell_size:(i + 1) * self.cell_size,
                                 j * self.cell_size:(j + 1) * self.cell_size]
                cell_angle = gradient_angle[i * self.cell_size:(i + 1) * self.cell_size,
                             j * self.cell_size:(j + 1) * self.cell_size]

                #得到每一个cell的梯度直方图;
                cell_gradient_vector[i][j] = self.cell_gradient(cell_magnitude, cell_angle)

        #得到HOG特征可视化图像
        hog_image = self.render_gradient(np.zeros([height, width]), cell_gradient_vector)

        #HOG特征向量
        hog_vector = []
        #使用滑动窗口
        for i in range(cell_gradient_vector.shape[0] - 1):
            for j in range(cell_gradient_vector.shape[1] - 1):
                #4个cell得到一个block
                block_vector = cell_gradient_vector[i:i+1][j:j+1].reshape(-1, 1)
                #正则化
                block_vector = np.array([vector / np.linalg.norm(vector) for vector in block_vector])


                hog_vector.append(block_vector)
        return hog_vector, hog_image

    def global_gradient(self):
        #得到每个像素的梯度
        gradient_values_x = cv2.Sobel(self.img, cv2.CV_64F, 1, 0, ksize=5)#水平
        gradient_values_y = cv2.Sobel(self.img, cv2.CV_64F, 0, 1, ksize=5)#垂直
        gradient_magnitude = np.sqrt(gradient_values_x**2 + gradient_values_y**2)#总
        gradient_angle = cv2.phase(gradient_values_x, gradient_values_y, angleInDegrees=True)#方向
        return gradient_magnitude, gradient_angle

    def cell_gradient(self, cell_magnitude, cell_angle):
        #得到cell的梯度直方图
        orientation_centers = [0] * self.bin_size
        for i in range(cell_magnitude.shape[0]):
            for j in range(cell_magnitude.shape[1]):
                gradient_strength = cell_magnitude[i][j]
                gradient_angle = cell_angle[i][j]
                min_angle, max_angle, mod = self.get_closest_bins(gradient_angle)
                orientation_centers[min_angle] += (gradient_strength * (1 - (mod / self.angle_unit)))
                orientation_centers[max_angle] += (gradient_strength * (mod / self.angle_unit))
        return orientation_centers

    def get_closest_bins(self, gradient_angle):
        idx = int(gradient_angle / self.angle_unit)
        mod = gradient_angle % self.angle_unit
        return idx, (idx + 1) % self.bin_size, mod

    def render_gradient(self, image, cell_gradient):
        #得到HOG特征图
        cell_width = self.cell_size / 2
        max_mag = np.array(cell_gradient).max()
        for x in range(cell_gradient.shape[0]):
            for y in range(cell_gradient.shape[1]):
                cell_grad = cell_gradient[x][y]
                cell_grad /= max_mag
                angle = 0
                angle_gap = self.angle_unit
                for magnitude in cell_grad:
                    angle_radian = math.radians(angle)
                    x1 = int(x * self.cell_size + magnitude * cell_width * math.cos(angle_radian))
                    y1 = int(y * self.cell_size + magnitude * cell_width * math.sin(angle_radian))
                    x2 = int(x * self.cell_size - magnitude * cell_width * math.cos(angle_radian))
                    y2 = int(y * self.cell_size - magnitude * cell_width * math.sin(angle_radian))
                    cv2.line(image, (y1, x1), (y2, x2), int(255 * math.sqrt(magnitude)))
                    angle += angle_gap
        return image

img = cv2.imread('/home/hichens/Desktop/bolt.jpg', cv2.IMREAD_GRAYSCALE) # 灰度图片
hog = Hog_descriptor(img, cell_size=8, bin_size=9)
vector, image = hog.extract()
print (np.array(vector).shape)
plt.subplot(121)
plt.imshow(img, cmap=plt.cm.gray)
plt.subplot(122)
plt.imshow(image, cmap=plt.cm.gray)
plt.show()