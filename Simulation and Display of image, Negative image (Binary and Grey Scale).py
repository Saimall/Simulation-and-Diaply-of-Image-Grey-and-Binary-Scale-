#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[3]:


import cv2
import matplotlib.pyplot as plt


# In[4]:


k = cv2.imread("joseph.png")


# In[4]:


cv2.imshow("original image",k)
cv2.waitKey(0)


# In[5]:


igrey=cv2.cvtColor(k,cv2.COLOR_BGR2GRAY)


# In[8]:


cv2.imshow("Grey",igrey)
cv2.waitKey(0)


# In[6]:


ret,bw_img = cv2.threshold(igrey,127,255,cv2.THRESH_BINARY)


# In[10]:


cv2.imshow("Binary Image",bw_img)
cv2.waitKey(0)


# In[7]:


height,width,_ = k.shape


# In[10]:


for i in range(0,height-1):
    for j in range(0,width-1):
        #get the pixel value 
        pixel=k[i,j]
        #negate each channel by subracting it from 255
        
        #1st index contains red pixel
        pixel[0]=255-pixel[0]
        
        #2nd index contains green pixel
        pixel[1]=255-pixel[1]
        
        #3rd index contains blue pixel
        pixel[2]=255-pixel[2]
        
        #store new values in pixel
        k[i,j]=pixel


# In[11]:


plt.imshow(k)
plt.show()
cv2.waitKey()


# In[ ]:




