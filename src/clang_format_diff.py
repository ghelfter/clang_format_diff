#!/usr/bin/env python3

# Copyright 2018 Galen Helfter
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

""" Main executable for the graphical diff program. """

import sys
import os

import display.window

from core.core import Core
from core.log import Logger

def print_version():
    """ Prints the version and program name to standard out """
    print('{}, version {}'.format(Core.PROGRAM_NAME, Core.VERSION))

def print_usage():
    """ Prints the program usage out to standard out """
    print('USAGE: {} [options]'.format(os.path.basename(__file__)))

def main(argv):
    """ Main application function, program point of entry """

    # Go through any arguments
    to_exit = False

    if len(argv) > 1:
        for arg in argv:
            if arg == '--version':
                to_exit = True
                print_version()
                break
            elif arg == '-h' or arg == '--help':
                to_exit = True
                print_usage()
                break

    # After finishing loading and setup, go down into the main display loop
    if not to_exit:
        # Initialize core and start logging system
        app_core = Core.get_core()
        log_path = os.path.join(os.getcwd(), 'app_log.txt')
        app_core.logger = Logger(log_path)
        app_core.logger.log('Format diff startup')

        display.window.run(argv)

if __name__ == '__main__':
    main(sys.argv)
