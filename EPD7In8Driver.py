import argparse
import json
import logging
import os

from PIL import Image, ImageDraw, ImageFont

from IT8951 import constants
from IT8951.display import AutoEPDDisplay

EPD7IN8WIDTH = 1872
EPD7IN8HEIGHT = 1404
EPD7IN8FREQ = 24000000  # 24 MHz SPI frequency
EPD7IN8VCOM = -1.4  # Find this number on the cable


class EPD7In8Driver:
    def __init__(self, config, virtual=False, rotate=None):
        self.width = EPD7IN8WIDTH
        self.height = EPD7IN8HEIGHT
        if virtual:
            from IT8951.display import VirtualEPDDisplay

            self.disp = VirtualEPDDisplay(
                dims=(self.width, self.height), rotate=rotate
            )
        else:
            logging.info('Initializing 7.8 inch e-paper display.')
            self.disp = AutoEPDDisplay(vcom=-1.4, rotate=rotate, spi_hz=EPD7IN8FREQ)
            logging.info(f'VCOM set to {self.disp.epd.get_vcom()}')


    def clear_frame(self):
        '''Fill the frame with white dot
        Note: clear_frame is different from disp.clear(). The latter will write the data to the display hardware.
        '''
        self.disp.frame_buf.paste(0xFF, box=(0, 0, self.width, self.height))


    def show_one_image(self, img):
        '''Input: img, an PIL object'''
        self.clear_frame()

        dims = (self.width, self.height)
        img.thumbnail(dims)
        paste_coords = [dims[i] - img.size[i] for i in (0,1)]  # align image with bottom of display
        self.disp.frame_buf.paste(img, paste_coords)

        self.disp.draw_full(constants.DisplayModes.GC16)

    def display_text(self):
        pass
