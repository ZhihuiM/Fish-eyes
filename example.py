from api import Detector
from PIL import Image


# Initialize detector
detector = Detector(model_name='rapid',
                    weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                    use_cuda=False)


# A simple example to run on a single image and plt.imshow() it

# detector.detect_one(img_path='./images/exhibition.jpg',
#                     input_size=1024, conf_thres=0.3,
#                     visualize=True)


# A simple example to run on a single image and save it

image = detector.detect_one(img_path='./input_images/exhibition.jpg', return_img=True,
                         input_size=1024, conf_thres=0.3, test_aug=None, )

Image.fromarray(image,'RGB').save('./output_images/output_RAPid/exhibition.jpg')
