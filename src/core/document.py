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

""" Contains operations and definitions for working with documents """

import os.path

class Document:
    """ Stores the information referring to a document, either one that is
        physically on a machine or one created in memory. """

    def __init__(self, filepath=None):
        self.filepath = filepath
        self._data = None

    def is_virtual(self):
        """ Returns true if the filepath is not valid and the document refers
            to no currently existing file on disk """
        return self.filepath is None or not os.path.isfile(self.filepath)

    def commit(self):
        """ If the document currently has data loaded in memory, will commit
            it back out to its filepath. Will perform no action if data is
            None or if the document has no valid associated filepath """
        # To do: Make this run if even if the path isn't existing, as it could
        # be the first time it's written to
        if not self.is_virtual() and self._data is not None:
            with open(self.filepath, 'w') as out_file:
                for line in self._data:
                    out_file.write(line)

    def load(self):
        """ Loads the file in from disc into a list of lines """
        if not self.is_virtual():
            with open(self.filepath, 'r') as in_file:
                self._data = []
                for line in in_file:
                    self._data.append(line)


def splice(first, second, sections):
    """ Given two documents and the sections for each, splices them together.
        The sections list is expected to be a tuple of three integers, with
        the first being the document, 0 for first, 1 for second, and the other
        two terms being the start and end lines. """
    doc = Document()

    return doc
