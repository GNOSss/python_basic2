import os
import time


mtime = os.path.getmtime('/Users/seungsoosmacbook/Desktop/python/python_yalco/sec13/chap01/fruits/apple.txt')
print(time.ctime(mtime))