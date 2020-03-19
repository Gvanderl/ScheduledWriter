import config
import matplotlib.pyplot as plt
import numpy as np

max_green = 21
image = np.ones((len(config.image), len(config.image[0]), 3))
green = 1 - (np.array(config.image) / max_green)
np.place(image[:, :, 0], green < 1, 0)
np.place(image[:, :, 2], green < 1, 0)
image[:, :, 1] = green
plt.imshow(image)
plt.show()
