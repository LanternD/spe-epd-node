import argparse
import json
import logging

from AppInstagramShowcase import AppInstagramShowcase
from EPD7In8Driver import EPD7In8Driver

logging.basicConfig(
    format="\033[92m[%(levelname)s]\033[00m %(message)s", level=logging.INFO
)


def parse_args():
    """Copy from https://github.com/GregDMeyer/IT8951/blob/master/test/integration/test.py"""
    p = argparse.ArgumentParser(description="Test EPD functionality")
    p.add_argument(
        "-v",
        "--virtual",
        action="store_true",
        help="display using a Tkinter window instead of the "
        "actual e-paper device (for testing without a "
        "physical device)",
    )
    p.add_argument(
        "-r",
        "--rotate",
        default=None,
        choices=["CW", "CCW", "flip"],
        help="run the tests with the display rotated by the specified value",
    )
    return p.parse_args()


def app_ins_main():

    args = parse_args()

    try:
        f_json = open("./config.json", "r")
        config = json.load(f_json)
    except FileNotFoundError:
        logging.error("config.json file not found. Terminated.")
        return

    if not args.virtual:
        epd = EPD7In8Driver(config=config, virtual=False)
    else:
        epd = EPD7In8Driver(config=config, virtual=True)

    ins_app = AppInstagramShowcase(config, epd)
    # ins_app.get_ins_photo_list()
    ins_app.app_pipeline()


if __name__ == "__main__":
    app_ins_main()
