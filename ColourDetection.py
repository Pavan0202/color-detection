#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import pandas as pd
import numpy as np


# In[ ]:


img_path = "E:\ThirdYear\Extr\Project\Colour_detecion\colorpic.jpg"
csv_path = "E:\ThirdYear\Extr\Project\Colour_detecion\colors.csv"


# In[ ]:


# reding csv files
index = ['color','color_name','hex','R','G','B']


# In[ ]:


df = pd.read_csv(csv_path , names=index , header = None)


# In[ ]:


# reading image
img = cv2.imread(img_path)
img = cv2.resize(img , (800,600))


# In[ ]:


#declaraing global variables
clicked = False
r = g = b = xpos = ypos = 0


# In[ ]:


#function for calculating minimum distance from all color and get matching color
def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i , 'color_name']
        return cname


# In[ ]:


#Function to get X and Y coordinate of mouse double click
def draw_function(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[ ]:


#creting window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)


# In[ ]:


while True:
    cv2.imshow('image',img)
    if clicked:
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (600,60), (b,g,r), -1)
        
        #creating text storing to display( color name and RGB values)
        text = get_color_name(r,g,b)+ 'R='+ str(r) + 'G=' + str(g) + 'B=' +str(b)
        
        cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)
        
        #for very light colours 
        if r+g+b >= 600:
            cv2.putText(img,text,(50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


# In[ ]:




