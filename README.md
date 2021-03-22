# spe-epd-node

"spe" stands for "seven point eight", corresponding to the e-ink screen size.

7.8-inch e-paper display control. 

# Resources for Development

## Where to buy

I bought my screen on [AliExpress](https://www.aliexpress.com/item/4000033507611.html?spm=a2g0s.9042311.0.0.26814c4divIUBO). 

## Datasheet

- 7.8 inch e-Paper datasheet: https://www.waveshare.com/w/upload/b/b4/7.8inch_e-Paper_Specification.pdf
- Adapter schematic: https://www.waveshare.com/wiki/File:7.8-10.3inch-e-Paper-Adapter-Schematic.pdf

For more, read the "Datasheet" folder.

## Wiki

Link: [7.8inch e-Paper HAT](https://www.waveshare.com/wiki/7.8inch_e-Paper_HAT?spm=a2g0o.detail.1000023.1.568b1822g6Skel&file=7.8inch_e-Paper_HAT)

(Deprecated, see below) Please install the driver according to the wiki.

## IT8951 Driver

The driver in wiki is c-based, meaning that you need to develop your code with C. We can change the driver to python-based.

 The principle is the same: control the SPI port of Raspberry Pi to send the data to the IT8951 chip on the hat.

I recommand this: https://github.com/GregDMeyer/IT8951

To verify, run `.test/integration/test.py`. This is even faster than the C-based driver (bcm2835) in the wiki.

Now you can develop your code with python.

# Config File

The configuration is stored in `config.json` file. It contains personal data so please update the fields accordingly in `config_example.json`. Then rename it to `conig.json`.

# App 1: Instagram showcase

This app displays a random Instagram image from a given user.

Please set the folder name in `config.json`. If your photo is in `/home/your_name/instagram/my_ins_id/`, then the field should be set to `instagram/my_ins_id/`.


