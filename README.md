# fish-eyes

We collected some algorithms for fish eye image de distortion.  
Including RAPid and some traditional algorithms (checkboard, horizontal expansion, latitude, longitude).

## Folder Structure

'input_images': Put the fisheye images that need to be de distorted in this folder.  
'output_images': Output images of different algorithms will be stored here (corresponding subfolder).  
'utils', 'models', 'weight': Files about RAPiD model.  
'Traditional_methods': Four different traditional algorithms.  


## Run RAPiD algorithm Demo (Using single image):
step1. Put source image in folder 'input_images'.
step2. Modify the image path and name in 'example.py' and run it.  
step3. View the output image in folder 'output_images/output_RAPiD'

