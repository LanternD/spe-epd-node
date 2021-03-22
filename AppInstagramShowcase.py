import logging
import random
import time
from os.path import expanduser

from PIL import Image, ImageDraw, ImageFont

from EPD7In8Driver import EPD7In8Driver
from utils import get_file_list


class AppInstagramShowcase:
    def __init__(self, config, drv):
        self.epd_drv = drv
        self.home_folder = expanduser("~") + "/"
        self.ins_folder = self.home_folder + config["instagram_photo_dir"]
        self.photo_list = self.get_ins_photo_list()

    def get_ins_photo_list(self):
        photo_fn_list = get_file_list(self.ins_folder)
        # print(self.home_folder+self.ins_folder)
        # print(len(photo_list), photo_list[:10])
        if len(photo_fn_list) == 0:
            logging.error("The Ins folder is empty.")

        return photo_fn_list

    def show_one_ins_image(self, pic_path):
        img = Image.open(pic_path)
        self.epd_drv.show_one_image(img)

    def app_pipeline(self):
        while True:
            rand_path = random.choice(self.photo_list)
            logging.info(f'Display: {rand_path}')
            self.show_one_ins_image(self.ins_folder+rand_path)
            time.sleep(10)
