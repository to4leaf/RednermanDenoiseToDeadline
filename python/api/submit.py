#-*- coding:utf-8 -*-
import os
import sys
import re
import json
from datetime import datetime

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# Ww_Deadline
import DenoiseToDeadline
reload(DenoiseToDeadline)
import deadline_common_api
reload(deadline_common_api)


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Submit():   
    def __init__(self, current_scene, project_dict, render_dict, uesr_dict, pool_name, second_pool_name, group_name, priority, frame_per_task, machine_limit, delayed, step, memo):
        #         
        self.current_scene = current_scene
        self.project_dict = project_dict               
        self.render_dict = render_dict
        # user
        self.user_id = uesr_dict['sg_ww_id']
        self.user_name = uesr_dict['name']
        # fram setting
        self.pool_name = pool_name
        self.second_pool_name = second_pool_name
        self.group_name = group_name
        self.priority = priority
        self.frame_per_task = frame_per_task
        self.machine_limit = machine_limit
        self.delayed = delayed
        self.step = step
        self.memo = memo


    # deadline                       
    def submit_job_info(self, w_deadline, sub_name, frame, cmds):          
        w_deadline.set_job_info_name('python', 'denoise', sub_name, frame)
        
        w_deadline.job_info["Pool"] = self.pool_name
        w_deadline.job_info["SecondaryPool"] = self.second_pool_name
        w_deadline.job_info["Priority"] = self.priority
        w_deadline.job_info["Group"] = self.group_name
        w_deadline.job_info["MachineLimit"] = self.machine_limit
        w_deadline.job_info["UserName"] = self.user_id
        w_deadline.job_info["Comment"] = self.memo        
        w_deadline.job_info["JobDependencies"] = None        
        #chunksize
        chunk = 10 if 'primary' in sub_name else 2 if 'LPE' in sub_name else 1        
        w_deadline.job_info["ChunkSize"] = chunk
        # delay job
        if self.delayed:
            w_deadline.job_info["ScheduledType"] =  "Once"
            w_deadline.job_info["ScheduledStartDateTime"] = self.delayed
        # step frame
        _frame = "%sstep%s"%(str(frame), self.step)
        w_deadline.job_info["Frames"] = _frame
        
        w_deadline.plugin_info["Executable"] = 'python'
        w_deadline.plugin_info["Arguments"] = ' '.join(cmds + ['{}-{}'.format('<STARTFRAME>', '<ENDFRAME>')])

        return w_deadline.submit_job()
        

    def submit_job_rename(self, w_deadline, sub_name, cmds, main_job):        
        w_deadline.set_job_info_name('python', 'rename', sub_name)
        
        w_deadline.job_info["JobDependencies"] = main_job.get("_id")
        w_deadline.job_info["Frames"] = "" 
        w_deadline.plugin_info["Executable"] = 'python'
        w_deadline.plugin_info["Arguments"] = ' '.join(cmds)
        w_deadline.submit_job()


    def submit(self):
        # 파이썬 가져오기
        _filepath = DenoiseToDeadline._filepath()
        rename_py = 'python/api/rename_to_fram.py'
        rename_path = os.path.join(_filepath, rename_py)        
        convert_py = 'python/api/convert_denoise_cmd.py'
        convert_path = os.path.join(_filepath, convert_py)
        
        if os.path.isfile(rename_path) and os.path.isfile(convert_path):
            split_path = self.current_scene.split(os.sep)
            file_title = os.path.join(split_path[-2], split_path[-1])                    
            # submit job to deadline
            w_deadline = deadline_common_api.WDeadline()
            _timestamp = get_timestamp()
            w_deadline.set_job_info_batchname(str(_timestamp), 
                                                                    self.project_dict['project'],
                                                                    str(self.user_name),
                                                                    self.project_dict['shot'],
                                                                    self.project_dict['version'],                                                                    
                                                                    file_title)
                         
            # get data
            denoise_path = self.render_dict['denoise_path']
            variance_path = self.render_dict['variance']
            strength = self.render_dict['flag']['strength']             
            total_frame = self.render_dict['frame']['total_frame']                  
            fixed_frame = self.render_dict['frame']['fixed_frame']           
            if not fixed_frame:
                fixed_frame = total_frame
                
            for key, value in self.render_dict['order'].items()[::-1]:                
                title_name = value['denoise']['name']
                out_path = value['denoise']['out_path']
                out_dir = value['denoise']['out_dir']
                # denoise
                denoise_cmd = [convert_path, title_name, denoise_path, total_frame, variance_path, out_path, out_dir,strength]
                main_job = self.submit_job_info(w_deadline, title_name, fixed_frame, denoise_cmd)                
                # rename
                if value['rename']:       
                    old_name =  value['rename']['old']
                    new_name = value['rename']['new']                                             
                    rename_cmd = [rename_path, out_dir,  old_name, new_name, fixed_frame]                    
                    self.submit_job_rename(w_deadline, title_name, rename_cmd, main_job)      
                  
            printInfo = '팜에 정상적으로 날아갔습니다.'
            QMessageBox.information(None, 'Warning', printInfo)         
                                                                  
        else:
            printInfo = 'python 파일을 찾지 못했습니다.'
            QMessageBox.warning(None, 'Warning', printInfo)                 
            raise ValueError(printInfo)
                
                
                
                
                
                
                
                
                
                




                
                
                

