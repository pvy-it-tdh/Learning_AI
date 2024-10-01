import numpy as np
# Khai báo mảng
a = np.array([1, 3, 3, 7])
# Hiển thị số chiều của mản
print(a.ndim) # 1 chiều
a = np.array([[1, 3, 3, 7],[5, 2, 4, 6]])
print(a.ndim)# 2 chiều
a0 = a[0]#[1, 3, 3, 7]
# Lấy phần tử a[0] từ 0 đến 2
print(a[0][:3])
# Hiển thị số hàng và số cột
print(a.shape)
# Độ dài mảng
print(len(a[0]))
