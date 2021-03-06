#
# Options.py
#
# Copyright (c) 2019 Stale Pixels All rights reserved.
#

from __future__ import print_function

PRINT_MODE_NEW = 0              ## Waiting for a new command
PRINT_MODE_TXT = 1              ## Printing Text
PRINT_MODE_SCR = 2              ## Printing a SCR
PRINT_MODE_NXI = 3              ## Printing a NXI

PRINT_MODE_CMD = -1             ## Processing a Command

class Options:
    """ """
    printer_width = 256
    printer_height = 192
    printer = None
    logfile = None
    temppath = "/tmp"

    def __init__(self, args):
        if args.printer_width:
            self.printer_width = args.printer_width
        else:
            self.printer_width = args.printer_width
        if args.printer_height:
            self.printer_height = args.printer_height
        if args.logfile:
            self.logfile = args.logfile
        self.printer = args.printer

class PrintJobOptions:
    """ """
    mode = PRINT_MODE_NEW
    size = 0
    dither = False
    rotate = False
    cmd = ""
    done = False
    args = None

    def __init__(self, args):
        """ """
        self.args = args

# Ensure that BasicPrint is ran in a stand-alone fashion (as intended) and not
# imported as a module. Prevents accidental execution of code.
if __name__ == '__main__':
    """ """
    print ("Nope")

