  #!/usr/bin/python3
# regex.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '\_/\_/', line), end = '')
     
if __name__ == "__main__": main()
