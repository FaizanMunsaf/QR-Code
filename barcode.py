# -*- coding: utf-8 -*-
"""
Create a Barcode

@author: Faizan_Munsaf
"""

import pyqrcode
from pyqrcode import QRCode

QRstring = "https://linktr.ee/autoquiz"
url = pyqrcode.create(QRstring)

url.png("autoquiz.png", scale=8)