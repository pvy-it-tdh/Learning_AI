import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread("anh.jpg")
# Cắt ảnh về 200x200
img = cv2.resize(img, (200, 200))
# Convert sang ảnh xám
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)


class Conv2d:
    def __init__(self, input, kernelSize):
        self.input = input
        self.height, self.width = input.shape
        self.kernel = np.random.randn(kernelSize, kernelSize)
        self.result = np.zeros((self.height - kernelSize + 1, self.width - kernelSize + 1))

    def getROI(self):
        for row in range(self.height - self.kernel.shape[0] + 1):
            for col in range(self.width - self.kernel.shape[1] + 1):
                roi = self.input[row:row + self.kernel.shape[0], col:col + self.kernel.shape[1]]
                yield row, col, roi

    def operate(self):
        for row, col, roi in self.getROI():
            self.result[row, col] = np.sum(roi * self.kernel)
        return self.result


# Tạo đối tượng Conv2d và thực hiện convolution
conv2d = Conv2d(img_gray, 3)
img_gray_conv2d = conv2d.operate()

# Hiển thị ảnh sau khi áp dụng convolution
plt.imshow(img_gray_conv2d, cmap='gray')
plt.show()
