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

# Append source directory so that tests can easily exist outside
sys.path.append('../src')

from core.configure.configuration import Configuration

class TestConfiguration(unittest.TestCase):
    """ Test the core module in the core library """

    def test_1_fail_load(self):
        """ Test that configuration fails on empty file """
        config = Configuration()
        self.assertFalse(config.load())

    def test_2_open_load(self):
        """ Test success on an empty file """
        filepath = './test_config.txt'
        if os.path.isfile(filepath):
            os.unlink(filepath)

        # Create file
        with open(filepath, 'w') as out_file:
            pass

        self.assertTrue(os.path.isfile(filepath))

        config = Configuration(filepath)
        self.assertTrue(config.load())

        if os.path.isfile(filepath):
            os.unlink(filepath)

    def test_3_invalid_file(self):
        """ Test a file that does not exist """
        filepath = './test_config.txt'
        if os.path.isfile(filepath):
            os.unlink(filepath)

        config = Configuration(filepath)
        self.assertFalse(config.load())

if __name__ == '__main__':
    unittest.main()
