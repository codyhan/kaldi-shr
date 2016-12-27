#!/usr/bin/env python
# coding: utf-8

import random
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

import sys
import os

reload(sys)
sys.setdefaultencoding( "utf-8" )


#text = u"这是一段测试文本，test 123。"
 
#im = Image.new("RGB", (300, 50), (255, 255, 255))
#dr = ImageDraw.Draw(im)
#font = ImageFont.truetype(os.path.join("fonts", "yuhongliang.ttf"), 14)
 
#dr.text((10, 5), text, font=font, fill="#000000")
 
#im.show()
#im.save("t.png")

path_pic = sys.argv[1]
func = sys.argv[2]

image_rgb = Image.open(path_pic) 
image_gray = image_rgb.convert('L')
w, h = image_gray.size
if h != 64:  
    
    h0 = 48
    w0 = int(round(1.0 * h0 / h * w)) + 1
    image_gray_new = image_gray.resize((w0, h0), Image.ANTIALIAS)

    h = 64
    w = int(round(1.0 * h / h0 * w0)) + 1
    image_gray = Image.new('L', (w, h), 'white')
    image_gray.paste(image_gray_new, (6,6), mask=None)

    w, h = image_gray.size
#image_gray.show()
#print str(w) + ' ' + str(h)
print func + '  [' 
flag = 1
iw = 0
win = 5
step = 3
while flag == 1:
    out = '  '
    for n in range(win):            
        for ih in range(h):
            if iw+n < w:
                out += str((255 - image_gray.getpixel((iw+n, ih)))) + ' '
            else:
                out += str(0) + ' '        
    if iw + step < w:
        iw += step
    else:  
        out += ']'          
        flag = 0
    print out.rstrip()

