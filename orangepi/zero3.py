# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI Zero 3
(see http://linux-sunxi.org/images/6/67/ORANGE_PI-ZERO-PLUS_V1_0_Schematic.pdf)

Usage:

.. code:: python
   import orangepi.zero3
   from OPi import GPIO

   GPIO.setmode(orangepi.zero3.BOARD)
"""

# pin number = (position of letter in alphabet - 1) * 32 + pin number
# So, PD14 will be (4 - 1) * 32 + 14 = 110

# Orange Pi Zero 3 physical board pin to GPIO pin
BOARD = {
    3:  229, # PH5/SDA/I2C3
    5:  228, # PH4/SCK/I2C3
    7:   73, # PC9
    8:  226, # PH2/TX/UART5
    10: 227, # PH3/RX/UART5
    11:  70, # PC6
    12:  75, # PC11
    13:  69, # PC5
    15:  72, # PC8
    16:  79, # PC15
    18:  78, # PC14
    19: 231, # PH7/MOSI/SPI1
    21: 232, # PH8/MISO/SPI1
    22:  71, # PC7
    23: 230, # PH6/CLK/SPI1
    24: 233, # PH9/CS/SPI1
    26:  74  # PC10
}

BCM = BOARD