#!/usr/bin/env python

from PIL import Image, ImageEnhance, ImageFont, ImageOps, ImageDraw
import textwrap


def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)


def overlay_demo(fname, n_pile, n_order):
    """Returns a watermarked version of input image, fname."""
    im = Image.open('./images/1024x768/' + fname)
    mark = Image.open('./images/1024x768/overlay.png')
    draw = ImageDraw.Draw(im)
    draw.text((44, 2), '%d,%02d' % (n_pile, n_order), font=ImageFont.load_default())    
    return watermark(im, mark, 'tile', 0.5)


def draw_wrapped_text(text):
    lines = textwrap.wrap(text, width = 40)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((w - width)/2, y_text), line, font = font, fill = FOREGROUND)
        y_text += height


def font_demo():
    FOREGROUND = (255, 255, 255)
    WIDTH = 375
    HEIGHT = 50
    TEXT = 'The plain Spain mainly falls down the drain.'
    #font_path = 'c:/windows/fonts/arial.ttf'
    font_path = '/Library/Fonts/Tahoma.ttf'
    font = ImageFont.truetype(font_path, 14, encoding='unic')
    text = TEXT.decode('utf-8')
    (width, height) = font.getsize(text)

    #x = Image.open('c:/temp/trashtestinput.png')
    x = Image.open('/tmp/trashtestinput.png')
    y = ImageOps.expand(x,border=2,fill=1)
    y = ImageOps.expand(y,border=30,fill=0)
    
    w, h = y.size
    bg = Image.new('RGBA', (w, 1000), "#000000")
    
    W, H = bg.size
    xo, yo = (W-w)/2, (H-h)/2
    bg.paste(y, (xo, 0, xo+w, h))
    draw = ImageDraw.Draw(bg)
    #draw.text(((w - width)/2, w), text, font=font, fill=FOREGROUND)
    lines = textwrap.wrap(text, width = 20)
    y_text = h
    for line in lines:
        width, height = font.getsize(line)
        draw.text(((w - width)/2, y_text), line, font = font, fill = FOREGROUND)
        y_text += height
    bg.show()
    fname_out = '/tmp/trashout.png'
    bg.save(fname_out)
    print 'wrote %s' % fname_out


def center_window_demo():
    x = 100
    y = 0
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    import pygame
    pygame.init()
    screen = pygame.display.set_mode((100, 100))

    # wait for a while to show the window.
    import time
    time.sleep(5)


if __name__ == '__main__':

    # # run font demo
    # font_demo()

    # # run overlay demo
    # n = range(1,14)
    # suits = ['c','d','s','h']
    # for s in suits[0]:
    #     for n in range(11,12):
    #         im = overlay_demo('%02d%s.gif' % (n,s), 0, n+14)
    #         im.show()

    center_window_demo()