import os
import sys


def call(self, args):
    has_url = len(args) > 2
    if not has_url:
        print("\nPlease provide a song/video name!\n")
        sys.exit(0)

    os.system(f"python3 {self.prefix}/share/felis/mp.py {args[1]} {' '.join(args[2:])}")
