"""Replacement for ``tail --follow --retry`` (or ``tail -F``)

The need for this tail replacement script came from the fact that ``tail -F``
doesn't work in Docker containers, at least when using certain storage drivers.

Usage::

    tailfr <file1> [<file2> ...]

"""


from __future__ import print_function
import os
import sys
import time


__version__ = '0.0.1'


def main():
    if len(sys.argv) < 2:
        print('Usage:\n'
              '\n'
              '    tailfr <file1> [<file2> ...]\n')
        sys.exit(1)
    try:
        stdout = sys.stdout.buffer  # Python 3.x
    except AttributeError:
        stdout = sys.stdout  # Python 2.x
    files = {}
    previous = None
    while True:
        got_new_data = False
        for path in sys.argv[1:]:
            if path not in files and os.path.exists(path):
                files[path] = open(path, 'rb')
            if path in files:
                data = files[path].read()
                if data:
                    got_new_data = True
                    if path != previous:
                        if previous:
                            stdout.write(b'\n')
                        stdout.write(b'==> ')
                        stdout.write(path.encode('UTF-8'))
                        stdout.write(b' <==\n')
                    previous = path
                    stdout.write(data)
                    stdout.flush()
        if not got_new_data:
            time.sleep(1)


if __name__ == '__main__':
    main()
