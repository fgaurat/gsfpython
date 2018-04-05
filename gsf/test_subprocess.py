# -*- coding: utf-8 -*-

import subprocess


if __name__ == "__main__":
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    print result.stdout