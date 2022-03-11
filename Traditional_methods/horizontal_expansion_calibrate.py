import cv2
import numpy as np
from tqdm import tqdm
from get_valid_area import get_valid_area

##水平展开法
##载入任意一张原图
image=cv2.imread('../input_images/25.jpg')
##提取有效圆形区域
image=get_valid_area(image)
print(image.shape)

if image.shape[0]!=image.shape[1]:
    raise ValueError('Image width isn\'t equal to height!')
##计算mapx和mapy并保存
R=image.shape[0]//2
W=int(2*np.pi*R)
H=R
mapx=np.zeros([H,W],dtype=np.float32)
mapy=np.zeros([H,W],dtype=np.float32)
for i in tqdm(range(mapx.shape[0])):
    for j in range(mapx.shape[1]):
        angle=j/W*np.pi*2
        radius=H-i
        mapx[i,j]=R+np.sin(angle)*radius
        mapy[i,j]=R-np.cos(angle)*radius
np.save('./npy/mapx2.npy',mapx)
np.save('./npy/mapy2.npy',mapy)


##载入remap矩阵和鱼眼原图，提取有效区域并做矫正
mapx=np.load('./npy/mapx2.npy')
mapy=np.load('./npy/mapy2.npy')
image=cv2.imread('../input_images/25.jpg')
image=get_valid_area(image)
image_remap=cv2.remap(image, mapx, mapy, interpolation=cv2.INTER_LINEAR,borderMode=cv2.BORDER_CONSTANT)
cv2.imwrite('../output_images/output_hroizontal/25.jpg',image_remap)