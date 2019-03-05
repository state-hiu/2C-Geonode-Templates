import shutil
import os

dst = '../static'
src = 'static'

try:
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src,dst)
except shutil.Error as exc:
    # handle any exception that might occur
    print("Got exception {} while copying {} to {}".format(exc, src, dst))

dst2 = '../templates'
src2 = 'templates'

try:
    if os.path.exists(dst2):
        shutil.rmtree(dst2)
    shutil.copytree(src2,dst2)
except shutil.Error as exc:
    # handle any exception that might occur
    print("Got exception {} while copying {} to {}".format(exc, src2, dst2))

