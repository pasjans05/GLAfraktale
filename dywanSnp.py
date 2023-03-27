import numpy as np
import matplotlib.pyplot as plt

def sierpinski_carpet(depth):

  if depth == 0:
    return np.ones((1, 1))

  carpet = sierpinski_carpet(depth - 1)
  center = np.zeros_like(carpet)
    
  squares = np.block([[carpet, carpet, carpet],
                      [carpet, center, carpet],
                      [carpet, carpet, carpet]])

  return squares

fig, ax = plt.subplots(figsize=(5, 5))

ax.set_aspect('equal')
ax.set_axis_off()

carpet = sierpinski_carpet(depth=2)

plt.imshow(carpet, cmap='binary')
plt.show()


# 1. import numpy as np: This line imports the numpy library and assigns it the alias "np". 
# 2. import matplotlib.pyplot as plt: This line imports the matplotlib library and assigns it the alias "plt".
# 3. def sierpinski_carpet(depth): This line defines a function called "sierpinski_carpet" that takes an argument called "depth".
# 4. if depth == 0: This line checks if the "depth" argument is equal to 0. 
# 5. return np.ones((1, 1)): This line returns an array of ones with shape (1,1) if the "depth" argument is equal to 0.
# 6. carpet = sierpinski_carpet(depth - 1): This line assigns the return value of the function "sierpinski_carpet" with argument "depth - 1" to the variable "carpet".
# 7. center = np.zeros_like(carpet): This line assigns an array of zeros with the same shape as the "carpet" variable to the variable "center".
# 8. squares = np.block([[carpet, carpet, carpet], [carpet, center, carpet], [carpet, carpet, carpet]]): This line creates an array of shape (3, 3) with the "carpet" and "center" variables as elements.
# 9. return squares: This line returns the array "squares".
# 10. fig, ax = plt.subplots(figsize=(5, 5)): This line creates a figure and assigns it to the variables "fig" and "ax".
# 11. ax.set_aspect('equal'): This line sets the aspect ratio of the figure to "equal".
# 12. ax.set_axis_off(): This line turns off the axes of the figure.
# 13. carpet = sierpinski_carpet(depth=2): This line assigns the return value of the function "sierpinski_carpet" with argument "depth=2" to the variable "carpet".
# 14. plt.imshow(carpet, cmap='binary'): This line creates an image from the "carpet" variable and sets the colormap to "binary".
# 15. plt.show(): This line displays the figure.