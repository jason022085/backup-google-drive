# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:54:45 2019

@author: USER
"""

import sys

cnt = 0
buf = []

def get_input():
    try:
        tbuf = input().split()
    except:
        raise Exception("No inputs")

    buf.extend(tbuf)
    global cnt
    cnt += len(tbuf)

    if len(tbuf)==0:
        get_input()

def get_str():
    global cnt
    if cnt==0:
        try:
            get_input()
        except:
            print("Error: No inputs")
            sys.exit()
            
    s = buf[0]
    buf.pop(0)
    cnt-=1
    return s

def get_int():
    while True:
        try:
            i = int( get_str() )
        except ValueError:
            print("Not int. Please try again")
            continue
        except :
            sys.exit()
        return i

def get_float():
    while True:
        try:
            f = float( get_str() )
        except ValueError:
            print("Not float. Please try again")
            continue
        except :
            sys.exit()
        return f
    
from mss import mss
import cv2 as cv
import numpy as np
from pyautogui import size

scale = 1

def setScale(r = 1):
    global scale
    scale = r

def getMatchTemplate(img, region):
    # detect box
    bbox={'left': region[0], 'top': region[1], 'width': region[2], 'height': region[3]}
    
    with mss() as sct:
        mss_im = sct.grab(bbox)
    im = np.array(mss_im.pixels,np.uint8)
    im = cv.cvtColor(im, cv.COLOR_RGB2BGR)
    result = cv.matchTemplate(im, img, 3)
    return result

def locateOnScreen(img, threshold=0.87, region=None):
    # init region
    if region == None:
        region = (0,0)+size()
        
    # faster read img
    if type(img) is not np.ndarray :
        img = cv.imread(img,cv.IMREAD_COLOR) # BGR Color
    
    result = getMatchTemplate(img,region)
    
    # get the most similar
    _minVal, maxVal, _minLoc, maxLoc = cv.minMaxLoc(result, None)
    
    if maxVal >= threshold:
        return (    maxLoc[0] // scale + region[0], 
                    maxLoc[1] // scale + region[1], 
                    img.shape[1] // scale, 
                    img.shape[0] // scale 
                )
    else:
        return None

def locateCenterOnScreen(img, threshold=0.87, region=None):
    # init region
    if region == None:
        region = (0,0)+size()
    
    # get the most similar 
    p = locateOnScreen(img,threshold,region)
    if p != None:
        p = ( p[0]+p[2]//2, p[1]+p[3]//2 ) # locate on center
    return p

def locateAllOnScreen(img, threshold=0.87, region=None):
    # init region
    if region == None:
        region = (0,0)+size()
    
    # faster read img
    if type(img) is not np.ndarray :
        img = cv.imread(img,cv.IMREAD_COLOR) # BGR Color
    
    result = getMatchTemplate(img,region)
    loc = np.where( result >= threshold )
    
    for pt in zip(*loc[::-1]):
        yield( (    region[0] + pt[0] // scale, 
                    region[1] + pt[1] // scale,
                    img.shape[1] // scale, 
                    img.shape[0] // scale
                ) )