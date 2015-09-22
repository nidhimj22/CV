import numpy as np 
import cv2
import math 

"""
def mymeanshift(dst, track_window, term_crit):
    return cv2.meanShift(dst, track_window, term_crit)

"""

# return new r,h,c,v, ret is true or false depending on continue to track or leave

def mymeanshift(dst, r , h, c, w, max_iter,threshold):
	radius = 1
	ret = True
	loss = 0
	r0 =  r
	h0 = h
        c0 = c
	w0 = w
	step = 1
	while step<max_iter:
    		step = step+1;
    		num_x = 0;
    		num_y = 0;
    		den = 0;
    		for i in h:
        		for j in w:
            			num_x = num_x+i*w(i,j)*gx(i,j);
            			num_y = num_y+j*w(i,j)*gy(i,j);
           		        den = den+w(i,j)*norm([gx(i,j) , gy(i,j)]);
       		if (abs(den-0)<threshold):
        		dx = round(num_x/den)
        		dy = round(num_y/den)
        		y0 = y0+dy;
 			x0 = x0+dx;
   
   		elif (y<1 || y>height-H) || (x<1 || x>width-W): # car is out of frame , stop tracking 
        		loss = 1
			ret = False
        		break
    		else:
    			dst1 = dst(r:r+w-1,c:c+h-1)
    			p = Density_estim(dst, dst1)

	return ret, (r0,h0,c0,w0)



def norm():

def w(i,j):

def g(i,j):


