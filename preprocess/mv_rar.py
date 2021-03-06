import glob
import os
import fnmatch
import shutil
import sys


def iterfindfiles(path, fnexp):
  for root, dirs, files in os.walk(path):
    for filename in fnmatch.filter(files, fnexp):
      yield os.path.join(root, filename)


i=0
for filename in iterfindfiles(r"./input/", "*.RAR"):
  i=i+1
  newfilename = "rar/" + str(i) + "_" + os.path.basename(filename)
  print(filename + " <===> " + newfilename)
  shutil.move(filename, newfilename)