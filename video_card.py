#!/usr/bin/python2
# -*- coding: utf-8 -*-

from display import SSD1306_Display
from PIL import Image, ImageDraw, ImageFont

#fa = fontawesome.font_awesome
#font = ImageFont.truetype('./testfont.ttf', 60)
#font = ImageFont.truetype('./DejaVuSans.ttf', 10)
#font = ImageFont.load_default()

# Display all icons
#for icon in fa.itervalues():
#    i = Image.new("1", (128,64))
#    d = ImageDraw.Draw(i, mode="1")
#    d.text((2,2), icon, fill=1, font=font)
#    dis.writeBuffer(dis.img2buffer(i.getdata()))
#    dis.displayBuffer()
#    del i
#    del d

class MyDisp():
    def __init__(self, w, h, wire, font_size=15):
        self.w = w
        self.h = h
        self.dis = SSD1306_Display(wire)
        self.dis.initDisplay()
        self.font = ImageFont.truetype('./Mechanical.otf', font_size)
        self.x = 0
        self.y = 0
        self.font_size = font_size
        self.image = None
        self.create_image("1")

    def create_image(self, mode):
        self.image = Image.new(mode, (self.w, self.h))

    def draw_text(self, text):
        d = ImageDraw.Draw(self.image, mode="1")
        d.text((self.x, self.y), text, fill=1, font=self.font)
        self.dis.writeBuffer(self.dis.img2buffer(self.image.getdata()))
        self.dis.displayBuffer()

    def draw_text_x_y(self, x, y, text):
        self.x = x
        self.y = y
        self.draw_text(text)

