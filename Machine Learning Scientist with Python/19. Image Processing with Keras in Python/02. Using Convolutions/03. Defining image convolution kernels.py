'''
Defining image convolution kernels
In the previous exercise, you wrote code that performs a convolution given an image and a kernel. This code is now stored in a function called convolution() that takes two inputs: image and kernel and produces the convolved image. In this exercise, you will be asked to define the kernel that finds a particular feature in the image.

For example, the following kernel finds a vertical line in images:

np.array([[-1, 1, -1], 
          [-1, 1, -1], 
          [-1, 1, -1]])
Instructions 1/3
33 XP
1
Define a kernel that finds horizontal lines in images.

2
Define a kernel that finds a light spot surrounded by dark pixels.

3
Define a kernel that finds a dark spot surrounded by bright pixels.
'''
SOLUTION

1
kernel = np.array([[-1, -1, -1], 
                   [1, 1, 1],
                   [-1, -1, -1]])


2
kernel = np.array([[-1, -1, -1], 
                   [-1, 1, -1],
                   [-1, -1, -1]])
                   
3
kernel = np.array([[1, 1, 1], 
                   [1, -1, 1],
                   [1, 1, 1]])