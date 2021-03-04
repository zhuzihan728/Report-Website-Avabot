

# img = cv2.imread('report/images/wave_shape3.png') # 读取照片
# img2 = cv2.imread('report/images/wave_shape4.png')
# rows, cols, channels = img.shape
# # 遍历每个像素点，进行颜色的替换
# for i in range(rows):
#   for j in range(cols):
#     print(img[i,j])
#     if img[i,j]==[255,255,255]: # 像素点: 255 = 白色
#       img2[i,j]=[235,245,255] # 白色 -> 青色

# cv2.imshow('img', img2)

import cv2

# 修改透明背景为白色
def transparence2white(img):
  sp=img.shape # 获取图片维度
  width=sp[0] # 宽度
  height=sp[1] # 高度
  for yh in range(height):
    for xw in range(width):
      color_d=img[xw,yh] # 遍历图像每一个点，获取到每个点4通道的颜色数据
      if(color_d[3]==255): # 最后一个通道为透明度，如果其值为0，即图像是透明
        img[xw,yh]=[255,245,235,255] # 则将当前点的颜色设置为白色，且图像设置为不透明
  return img

img=cv2.imread('report/images/wave_shape3.png',-1) # 读取图片。-1将图片透明度传入，数据由RGB的3通道变成4通道
img=transparence2white(img) # 将图片传入，改变背景色后，返回
cv2.imwrite('report/images/wave_shape4.png',img) # 保存图片，文件名自定义，也可以覆盖原文件