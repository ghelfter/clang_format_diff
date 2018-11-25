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

import unittest
import sys
import os
import os.path

# Append source directory so that tests can easily exist outside
sys.path.append('../src')

import core.log

def contains_line(filepath, line):
    """ Returns True if the file contains the given line """
    result = False

    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r') as in_file:
                for input_line in in_file:
                    if input_line == line:
                        result = True
        except:
            pass

    return result

class TestLog(unittest.TestCase):
    """ Test the log module in the core library """
    def test_1_log_create(self):
        """ Test that log file is created """
        log_path = './test_log.txt'
        logger = core.log.Logger(log_path)

        logger.log('Test')

        self.assertTrue(os.path.isfile(log_path))

        os.unlink(log_path)

    def test_2_log_content(self):
        """ Test that file contains written content """
        log_path = './test_log.txt'
        log_statement = 'Test log entry'
        logger = core.log.Logger(log_path)

        logger.log(log_statement)

        self.assertTrue(contains_line(log_path, log_statement + '\n'))

        os.unlink(log_path)

if __name__ == '__main__':
    unittest.main()
