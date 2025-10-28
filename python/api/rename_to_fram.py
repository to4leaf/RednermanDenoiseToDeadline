#-*- coding:utf-8 -*-
import os
import sys

out_dir = sys.argv[1]
old_name = sys.argv[2]
new_name = sys.argv[3]
total_frame = sys.argv[4] 

start, end = map(int, total_frame.split('-'))


for i in range(start, end + 1):
    old_path = old_name.format(path=out_dir, num=str(i))
    new_path = new_name.format(path=out_dir, num=str(i))

    if os.path.exists(old_path):
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)
        print('Rename Complete {} {} ; '.format(new_path, '-' * 30))
    else:
        pass

