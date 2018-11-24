#!/usr/bin/env python3
""" Main executable for the graphical diff program. """

import sys

import core.log
import display.window

def main(argv):

    # After finishing loading and setup, go down into the main display loop
    display.window.run(argv)

if __name__ == '__main__':
    main(sys.argv)
