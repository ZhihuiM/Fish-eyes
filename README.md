# fish-eyes

We collected some algorithms for fish eye image de distortion.  
Including RAPiD and some traditional algorithms (checkboard, horizontal expansion, latitude, longitude).

## Folder Structure

'input_images': Put the fisheye images that need to be de distorted in this folder.  
'output_images': Output images of different algorithms will be stored here (corresponding subfolder).  
'utils', 'models', 'weight': Files about RAPiD model.  
'Traditional_methods': Four different traditional algorithms.  


## Installation
**Requirements**:
The code should be able to work as long as you have the following packages:
- PyTorch >= 1.0. 
- numpy
- opencv-python  
- PIL
- shutil
- imutils
- tqdm
- pycocotools
- tensorboard (optional, only for training)  

## Run RAPiD algorithm Demo (Using single image)  

step1. Download the RAPiD [pre-trained network weights](https://drive.google.com/file/d/1NX3EJMFViNu9nMuNRFSygjKzGhAfLBmL/view?usp=sharing), which is trained on COCO, MW-R and HABBOF, and place it under the RAPiD/weights folder.
step2. Put source image in folder 'input_images'.  
step3. Modify the image path and name in `example.py` and run it.  
step4. View the output image in folder 'output_images/output_RAPiD'.  


## Run RAPiD algorithm Demo (Using video)  
step1. Download the RAPiD [pre-trained network weights](https://drive.google.com/file/d/1NX3EJMFViNu9nMuNRFSygjKzGhAfLBmL/view?usp=sharing), which is trained on COCO, MW-R and HABBOF, and place it under the RAPiD/weights folder.(If you have downloaded it before, skip this step.)
step2. Put source video in folder 'video'.  
step3. Modify the video path and name in `video_demo_RAPiD.py` and run it.  


## Run Traditional algorithms about distortion correction  

step1. Put source image in folder 'input_images'.  
step2. Modify the image path and name in corresponding algorithm file (`checkboard_calibrate.py`, `horizontal_expansion_calibrate.py`, `latitude_calibrate.py`, `longitude_calibrate.py`).  
step3. View the output image in corresponding subfolder under folder 'output_images'.
