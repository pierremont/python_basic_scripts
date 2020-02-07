#! /bin/python

import os
for root, dirnames, filenames in os.walk("/home/petrus/python"):
    print(filenames)
    break