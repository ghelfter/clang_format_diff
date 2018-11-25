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

import subprocess
import sys
import os.path

def main(argv):
    retcode = 0
    python_exe = 'python3'

    libraries = {'core' : ['log', 'document', 'core'],
                 'core.configure' : ['configuration']}

    success = True

    print('Running program tests\n')
    print('----------------------------------------------------------------------')
    print('----------------------------------------------------------------------\n')

    for library in libraries:
        library_dir = ''
        for elem in library.split('.'):
            library_dir = os.path.join(library_dir, elem)
        for module in libraries[library]:
            filename = module + '_test.py'
            python_file = os.path.join(library_dir, filename)

            res = subprocess.call([python_exe, python_file, '-v'])

            if res == 0:
                print(library + '.' + module + ' tests have passed.\n\n')
            else:
                success = False
                print(library + '.' + module + ' tests have failed.\n\n')

    if success:
        print('Tests have succeeded.')
    else:
        print('Tests have failed.')
        res = 1

    sys.exit(res)

if __name__ == '__main__':
    main(sys.argv)
