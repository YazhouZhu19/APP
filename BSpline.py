from PIL import Image
import numpy as np
from scipy import interpolate
from scipy.interpolate import BSpline


def BS_pline(img_array, original_values, target_values, k):

    t, c, k = interpolate.splrep(original_values, target_values, s=0, k=k)
    bspline = BSpline(t, c, k)
    transformed_img_array = bspline(img_array).clip(0, 255).astype(np.uint8)
    
    return transformed_img_array


img = Image.open('/home/cs4007/data/zyz/CDFSMIS/img.jpeg').convert('L')
img_array = np.array(img)


# 定义原始灰度值和目标灰度值
original_values = np.array([0, 64, 255], dtype=np.float32)
target_values = np.array([0, 80, 0], dtype=np.float32)
k = 2

transformed_img_array = BS_pline(img_array, original_values, target_values, k)


# 计算 B-spline 曲线的控制点，这里假设使用三次 B-spline
# k = 2
# t, c, k = interpolate.splrep(original_values, target_values, s=0, k=k)
# bspline = BSpline(t, c, k)

# # 读取图像并转化为灰度图
# img = Image.open('/home/cs4007/data/zyz/CDFSMIS/img.jpeg').convert('L')
# img_array = np.array(img)


# 对图像的每一个像素应用 B-spline 曲线进行映射
# transformed_img_array = bspline(img_array).clip(0, 255).astype(np.uint8)


# transformed_img_array = BSpline(img_array, original_values, target_values)


# 创建新的图像并保存
transformed_img = Image.fromarray(transformed_img_array)
transformed_img.save('/home/cs4007/data/zyz/CDFSMIS/transformed_image.jpg')



    


