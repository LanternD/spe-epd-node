import logging
import random
import time
from datetime import datetime, timedelta
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
        """Get all the files in the instagram folder. """
        photo_fn_list = get_file_list(self.ins_folder)
        # print(self.home_folder+self.ins_folder)
        # print(len(photo_list), photo_list[:10])
        if len(photo_fn_list) == 0:
            logging.error("The Ins folder is empty.")

        return photo_fn_list

    def show_one_ins_image(self, pic_path):
        """Show one image by a given absolute path."""
        img = Image.open(pic_path)
        self.epd_drv.show_one_image(img)

    def app_pipeline(self, interval=timedelta(minutes=10)):
        """The rountine to continuously display the photos."""

        def is_working_hour(dt):
            return (8, 59) < (dt.hour, dt.minute) < (23, 30)

        previous_update = datetime.now() - timedelta(minutes=10, seconds=1)
        while True:
            # Check every 15 seconds, update only during 9:00 - 23:30
            time_now = datetime.now()
            if time_now - previous_update > interval and is_working_hour(time_now):
                rand_path = random.choice(self.photo_list)
                time_str = time_now.strftime("%x %X")
                logging.info(f"[{time_str}] {rand_path}")
                self.show_one_ins_image(self.ins_folder + rand_path)
                previous_update = time_now
            time.sleep(15)
