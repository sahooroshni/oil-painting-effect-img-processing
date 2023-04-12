
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow
import random
from google.colab import drive
drive.mount('/content/drive')
img = cv2.imread('/content/drive/MyDrive/DIP/project/painting.png') cv2_imshow(img)
print(np.shape(img))
#Kuwahara filter implementation
def kuwahara(x,a):
# x = image on which filter is used, (2a + 1) = size of window
  a = int(a)
  n,m = x.shape
  x_kuw = np.zeros((n,m))
  for i in range(0,n):
    for j in range(0,m):
      quad_1 = []
      quad_2 = []
      quad_3 = []
      quad_4 = []
      for dx in np.arange(-a,1):
        for dy in np.arange(-a,1):
          if 0<=i+dx<n and 0<=j+dy<m:
              quad_1.append(x[i+dx,j+dy]) 
      quad_1 = np.array(quad_1)
      m1 = np.mean(quad_1)
      v1 = np.var(quad_1)
      
      
      for dx in np.arange(0,a+1):
        for dy in np.arange(-a,1):
          if 0<=i+dx<n and 0<=j+dy<m: 
              quad_2.append(x[i+dx,j+dy])
      quad_2 = np.array(quad_2)
      m2 = np.mean(quad_2)
      v2 = np.var(quad_2)

      for dx in np.arange(-a,1):
          for dy in np.arange(0,a+1):
              if 0<=i+dx<n and 0<=j+dy<m: quad_3.append(x[i+dx,j+dy])
      quad_3 = np.array(quad_3)
      m3 = np.mean(quad_3)
      v3 = np.var(quad_3)

      for dx in np.arange(0,a+1):
          for dy in np.arange(0,a+1):
              if 0<=i+dx<n and 0<=j+dy<m: quad_4.append(x[i+dx,j+dy])
      quad_4 = np.array(quad_4)
      m4 = np.mean(quad_4)
      v4 = np.var(quad_4)
      
      variance_list = [v1,v2,v3,v4] mean_list = [m1,m2,m3,m4]
      minimum = min(variance_list)
      pos = variance_list.index(minimum)
      x_kuw[i,j] = mean_list[pos] 
  return x_kuw

#applying kuwahara filter to the B, G and R components individually
b_kuw = kuwahara(img[:,:,0],6)
g_kuw = kuwahara(img[:,:,1],6)
r_kuw = kuwahara(img[:,:,2],6)

#merging R, G and B components
painting = np.dstack((b_kuw,g_kuw,r_kuw)) cv2_imshow(painting)#displaying final painting
