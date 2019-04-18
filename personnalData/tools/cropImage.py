from PIL import Image
import sys

im = Image.open(sys.argv[1])

im_size = im.size

left1,left2=0,im.size[0]/2
top1,top2=0,im.size[0]/2
height=im.size[0]/2
width=im.size[0]/2
box1,box2,box3,box4=(left1,top1,left1+width,top1+height),(left2,top1,left2+width,top1+height),(left1,top2,left1+width,top2+height),(left2,top2,left2+width,top2+height)

area1,area2,area3,area4=im.crop(box1),im.crop(box2),im.crop(box3),im.crop(box4)

area1.save("croped/1"+sys.argv[1],"JPEG")
area2.save("croped/2"+sys.argv[1],"JPEG")
area3.save("croped/3"+sys.argv[1],"JPEG")
area4.save("croped/4"+sys.argv[1],"JPEG")
