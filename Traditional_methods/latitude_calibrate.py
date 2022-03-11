import cv2
import numpy as np
from tqdm import tqdm
from get_valid_area import get_valid_area

#纬度法
##载入任意一张原图
image=cv2.imread('../input_images/25.jpg')
##提取有效圆形区域
image=get_valid_area(image)

if image.shape[0]!=image.shape[1]:
    raise ValueError('Image width isn\'t equal to height!')
##计算mapx和mapy并保存
R=image.shape[0]//2
mapx=np.zeros([2*R,2*R],dtype=np.float32)
mapy=np.zeros([2*R,2*R],dtype=np.float32)
for i in tqdm(range(mapx.shape[0])):
    for j in range(mapx.shape[1]):
        mapx[i,j]=j
        mapy[i,j]=(i-R)/R*(R**2-(j-R)**2)**0.5+R
np.save('./npy/mapx.npy',mapx)
np.save('./npy/mapy.npy',mapy)


##载入remap矩阵和鱼眼原图，提取有效区域并做矫正
mapx=np.load('./npy/mapx.npy')
mapy=np.load('./npy/mapy.npy')
image=cv2.imread('../input_images/25.jpg')
image=get_valid_area(image)
image_remap=cv2.remap(image, mapx, mapy, interpolation=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)
cv2.imwrite('../output_images/output_latitude/25.jpg',image_remap)

