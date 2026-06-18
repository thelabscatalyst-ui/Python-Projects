import numpy as np

# lets start by creating a random ultrasound image of size 128 by 128 pixels

np.random.seed(0) # for reproducibility
image = np.random.randint((128, 128), dtype = np.uint8) 
# unit8 means that the values will have range of values of 0 to 256, common for greyscale images. 

image[50:80, 50:80] = np.random.randint(220, 255, (30, 30)) # add a bright nodule for testing
# which we are assuming that it is a thyroid nodule.

def details (image):
    print("shape of the image is: " + np.shape(image))
    print("dtype of the image is: " + np.dtype(image))
    print("min pixel value is: " + np.min(image))
    print("max pixel value is: " + np.max(image))
    print("mean pixel value is: " + np.mean(image))

def normalization (image):
    return (image - np.min(image)) / (np.max(image) - np.min(image))

def standardization (image):
    return (image - np.mean(image)) / np.std(image) 

image_normalized = normalization(image)
image_standardized = standardization(image)
def masking(image_normalized):
    mask = (image_normalized > 0.7) & (image_normalized < 1.0) 
    return image_normalized[mask]

binary_mask = masking(image_normalized) # masked image is returned 
def count(binary_mask):
    # checking the number of white pixels in the binary mask
    white_count = 0

    for pixel in binary_mask:
        if(pixel == 1):
            white_count += 1

    total_pixels = 255
    return (white_count / total_pixels) * 100

def cropping(image_normalized):
    return image_normalized[32:96, 32:96] # cropping to the center 64x64 region

cropped = cropping(image_normalized)

def batch_process(cropped):
    # we will batch using numpy
    return cropped.reshape(1,64)

batch_ready = batch_process(cropped)