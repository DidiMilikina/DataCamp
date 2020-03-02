'''
Reducing noise
We have a noisy image that we want to improve by removing the noise in it.

Small cute puppy
Preloaded as noisy_image.
Use total variation filter denoising to accomplish this.

Instructions
100 XP
Import the denoise_tv_chambolle function from its module.
Apply total variation filter denoising.
Show the original noisy and the resulting denoised image.
'''
SOLUTION

# Import the module and function
from skimage.restoration import denoise_tv_chambolle

# Apply total variation filter denoising
denoised_image = denoise_tv_chambolle(noisy_image, 
                                      multichannel=True)

# Show the noisy and denoised images
show_image(noisy_image, 'Noisy')
show_image(denoised_image, 'Denoised image')