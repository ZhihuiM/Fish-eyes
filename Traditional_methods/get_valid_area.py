import cv2
import numpy as np

def get_valid_area(img):
    # 设置灰度阈值
    T = 40

    # 转换为灰度图片
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 提取原图大小
    rows, cols = img.shape[:2]
    print('image shape:',rows, cols)


    # 从上向下扫描
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if img_gray[i, j] >= T:
                if img_gray[i + 1, j] >= T:
                    top = i
                    break
        else:
            continue
        break
    #print('top =', top)


    # 从下向上扫描
    for i in range(rows - 1, -1, -1):
        for j in range(0, cols, 1):
            if img_gray[i, j] >= T:
                if img_gray[i - 1, j] >= T:
                    bottom = i
                    break
        else:
            continue
        break
    #print('bottom =', bottom)


    # 从左向右扫描
    for j in range(0, cols, 1):
        for i in range(top, bottom, 1):
            if img_gray[i, j] >= T:
                if img_gray[i, j + 1] >= T:
                    left = j
                    break
        else:
            continue
        break
    #print('left =', left)


    # 从右向左扫描
    for j in range(cols - 1, -1, -1):
        for i in range(top, bottom, 1):
            if img_gray[i, j] >= T:
                if img_gray[i, j - 1] >= T:
                    right = j
                    break
        else:
            continue
        break
    #print('right =', right)


    # 计算有效区域半径
    R = max((bottom - top) / 2, (right - left) / 2)
    #print('R =', R)


    # 提取有效区域
    img_valid = img[top:int(top + 2 * R), left:int(left + 2 * R)]
    #cv2.imwrite('./images/valid.jpg', img_valid)

    h = img_valid.shape[0]
    w = img_valid.shape[1]
    margin = int((w - h) / 2)

    img_valid = img_valid[:, margin:(margin + h):]
    print('cropped image shape:',img_valid.shape)

    return img_valid

def get_useful_area(image):
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,image_binary=cv2.threshold(image_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours,_=cv2.findContours(image_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour_fisheye=sorted(contours, key=cv2.contourArea, reverse=True)[0]
    center, radius = cv2.minEnclosingCircle(contour_fisheye)
    mask=np.zeros_like(image, dtype=np.uint8)
    mask=cv2.circle(mask, (int(center[0]), int(center[1])), int(radius), (1,1,1),-1)
    image_useful=image*mask
    image_fisheye=image_useful[int(center[1])-int(radius):int(center[1])+int(radius),int(center[0])-int(radius):int(center[0])+int(radius),:]
    return image_fisheye