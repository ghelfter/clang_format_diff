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
import os.path

sys.path.append('../src')

import core.document

class TestDocument(unittest.TestCase):
    """ Tests the document module in the core library """
    def test_1_is_real(self):
        """ Test document virtual status """

        # Document with no filepath
        doc1 = core.document.Document()
        self.assertTrue(doc1.is_virtual())

        # Document with invalid filepath
        path1 = 'test_not_valid_file.txt'
        self.assertFalse(os.path.isfile(path1))
        doc2 = core.document.Document(path1)
        self.assertTrue(doc2.is_virtual())

        # Document with valid filepath
        path2 = 'test_valid_file.txt'
        with open(path2, 'w') as test_file:
            pass
        self.assertTrue(os.path.isfile(path2))
        doc3 = core.document.Document(path2)
        self.assertFalse(doc3.is_virtual())

        os.unlink(path2)

if __name__ == '__main__':
    unittest.main()
