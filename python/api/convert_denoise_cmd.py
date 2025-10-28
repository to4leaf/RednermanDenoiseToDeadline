#-*- coding:utf-8 -*-
import os
import sys

# add path
sys.path.append('/westworld/inhouse/tool/rez-packages/PyYAML/3.10/python')
import yaml


# get argv
order_name = sys.argv[1]
denoise_path = sys.argv[2]
total_frame = sys.argv[3]
variance_path = sys.argv[4]
out_path = sys.argv[5]
out_dir = sys.argv[6]
strength = sys.argv[7]
fixed_frame = sys.argv[8]

start_frame, end_frame = map(int, fixed_frame.split('-'))


# get yaml
main_path =  os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
with open(main_path + '/resources/convert_info.yaml', 'r') as f:
    _load = yaml.safe_load(f)
    prman_ver = _load['renderman']['version']    
    prman_path = _load['renderman']['path']
    args = _load['denoise']['args']        


# get_flag
def get_flag(strength): 
    filter_json = os.path.join(main_path, 'resources/WW.filter.json')
    
    flag_cmd = []
    for arg in args:  
        flag_cmd.append(arg.format(filter_json = filter_json, strength_value = strength))
    
    return flag_cmd


def get_cross_frame(frame, total_frame):        
    start, end = map(int, total_frame.split('-'))
    total_len = end - start + 1

    if total_len == 1 or total_len== 2:
        return [''], [frame]            
    elif frame == start:
        return ['-L'], [frame, frame+1]      
    elif frame == end:
        return ['-F'], [frame-1, frame] 
    else:
        return  ['-F', '-L'], [frame-1, frame, frame+1]


# run
for frame in range(start_frame, end_frame + 1):
    print('Loading {} {} {} {}'.format(out_dir, order_name, frame, '-' * 30))

    cmds = []
    cmds += [prman_path.format(prman_ver, prman_ver)]
    cmds += ['--outdir', out_dir]     
    cmds += get_flag(strength)

    skip_frame, cross_frame = get_cross_frame(frame, total_frame)
    cmds += skip_frame

    if 'primary' not in order_name:      
        for cf in cross_frame:
            cmds.append(variance_path.format(path=denoise_path, num=cf))                        
                         
    for cf in cross_frame:
        cmds.append(out_path.format(path=denoise_path, num=cf))                   
        
    cmd = ' '.join(cmds)
    print('COMMAND : ' + cmd)    
    os.system(cmd)   















