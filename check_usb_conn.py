#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Written for unix machines, this module checks if an usb device is connected
    to the system or not. Works in both Python2.7 and Python 3.x environment.

    This module is more of a plugin as of now. In future, I will add more 
    features to it and will try to make it cross-platform compatible(Ahem!).
"""

from re import compile, I
import subprocess

__version__ = "1.0.0"
__author__ = "Sandeepan Bhattacharyya <bsandeepan95.work@gmail.com>"
__copyright__ = "Copyright 2019, Sandeepan Bhattacharyya"
__credits__ = ["Sandeepan Bhattacharyya", "Sandeepan Sengupta"]
__license__ = ""
__maintainer__ = "Sandeepan Bhattacharyya"
__email__ = "bsandeepan95.work@gmail.com"
__status__ = "Production"


def is_usb_connected(device_id):
    """ Checks if USB device with the provided DEVICE_ID is connected or not.
        If found, return TRUE, else FALSE. provide DEVICE_ID as found in
        terminal i.e. in 'vid:pid' format. Example: '12da:b65c'.
    """
    device_re = compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+)."
                           "+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", I)
    device_list = subprocess.check_output("lsusb")

    for i in device_list.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                if dinfo['id'] == device_id:
                    # found hence true
                    return True
    # for loop ended without return, hence not found so false
    return False


if __name__ == "__main__":
    # use this variable or whatever for maintaining desired device id
    required_device_id = '0781:5567'

    # use this code inside for loop
    if is_usb_connected(required_device_id):
        print("Is connected")
        # or run the code
    else:
        print("not found")
        # or exit the program
