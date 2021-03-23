# spe-epd-node

"spe" stands for "seven point eight", corresponding to the e-ink screen size.

7.8-inch e-paper display control. 

# Resources for Development

## Where to buy

I bought my screen on [AliExpress](https://www.aliexpress.com/item/4000033507611.html?spm=a2g0s.9042311.0.0.26814c4divIUBO). 

It relies on the IT8951 Hat to connect to Raspberry Pi.

## Datasheet

- 7.8 inch e-Paper datasheet: https://www.waveshare.com/w/upload/b/b4/7.8inch_e-Paper_Specification.pdf
- Adapter schematic: https://www.waveshare.com/wiki/File:7.8-10.3inch-e-Paper-Adapter-Schematic.pdf

For more, read the "Datasheet" folder.

## e-Paper Display Wiki

Link: [7.8inch e-Paper HAT](https://www.waveshare.com/wiki/7.8inch_e-Paper_HAT?spm=a2g0o.detail.1000023.1.568b1822g6Skel&file=7.8inch_e-Paper_HAT)

Please install the driver according to the wiki (Deprecated. Please use the below driver instead).

## IT8951 Driver

The driver in the wiki about is C-based, meaning that you need to develop your code with C. We can switch to a python-based driver.

The principle is the same: control the SPI port of Raspberry Pi to send the data to the IT8951 chip on the hat.

I recommand this: https://github.com/GregDMeyer/IT8951

To verify, run `.test/integration/test.py`. This is even faster than the C-based driver (bcm2835) in the wiki.

Now you can develop your code with python.

# Config File

The configuration is stored in `config.json`. It contains personal data so please update the fields accordingly in `config_example.json`. Then rename it to `conig.json`.

# App 1: Instagram showcase

This app displays a random Instagram image from a given user.

At this stage, the photos need to be stored in local. In the future, I may add the pipeline to fetch new photos from Instagram.

Please set the folder name in `config.json`. If your photo is in `/home/your_name/instagram/my_ins_id/`, then the field `instagram_photo_dir` should be set to `instagram/my_ins_id/`.


