import matplotlib.pyplot as plt

def disp_image(image):
  _, ax = plt.subplots(1, figsize=(16, 16))
  height, width = image.shape[:2]
  ax.set_ylim(height + 10, -10)
  ax.set_xlim(-10, width + 10)
  ax.axis('off')
  ax.imshow(image)
  plt.show()