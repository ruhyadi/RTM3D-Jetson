import shutil
import glob
import os

fns = sorted(glob.glob('/home/didi/Repository/RTM3D-Jetson/demo_kitti_format/data/kitti/my_image/*'))
src = '/home/didi/Repository/RTM3D-Jetson/demo_kitti_format/data/kitti/calib.txt'
dst = '/home/didi/Repository/RTM3D-Jetson/demo_kitti_format/data/kitti/my_calib/'

for i in range(len(fns)):
    shutil.copy(src, os.path.join(dst, f'{i:06d}.txt'))
