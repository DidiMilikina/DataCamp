'''
Help Sally restore her graduation photo
You are going to combine all the knowledge you acquired throughout the course to complete a final challenge: reconstructing a very damaged photo.

Help Sally restore her favorite portrait which was damaged by noise, distortion, and missing information due to a breach in her laptop.

Sally damaged picture
Sally's damaged portrait is already loaded as damaged_image.
You will be fixing the problems of this image by:

Rotating it to be uprightusing rotate()
Applying noise reduction with denoise_tv_chambolle()
Reconstructing the damaged parts with inpaint_biharmonic() from the inpaint module.
show_image() is already preloaded.

Instructions
100 XP

Import the necessary module to apply restoration on the image.
Rotate the image by calling the function rotate().
Use the chambolle algorithm to remove the noise from the image.
With the mask provided, use the biharmonic method to restore the missing parts of the image and obtain the final image.
'''
SOLUTION

# Import the necessary modules
from skimage.restoration import denoise_tv_chambolle, inpaint
from skimage import transform

# Transform the image so it's not rotated
upright_img = rotate(damaged_image, 20)

# Remove noise from the image, using the chambolle method
upright_img_without_noise = denoise_tv_chambolle(upright_img,weight=0.1, multichannel=True)

# Reconstruct the image missing parts
mask = get_mask(upright_img)
result = inpaint.inpaint_biharmonic(upright_img_without_noise, mask, multichannel=True)

show_image(result)