# -*- coding: utf-8 -*-
import os
import re
import sys
import glob
import yaml

from pprint import pprint 
from functools import partial
from datetime import datetime

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

# init
import DenoiseToDeadline
reload(DenoiseToDeadline)
#ww api
from ww_api import ww
reload(ww)
# ui
from ui import body_widget
reload(body_widget)
from deadline_option import SettingWidget
# api
from .api import submit
reload(submit)
from .api import make_dict
reload(make_dict)


class DenoiseApp(QDialog):    
    def __init__(self,config, parent=None):
        super(DenoiseApp, self).__init__(parent)

        # ww info
        self.ww = ww.Api(script_key="dept_pipeline", api_key="qeaagyjgysol~nbTcgkujfn2b")                 
        self.uesr_dict = self.get_user_dict()             
        
        # deadline setting
        self.job_pool = config["deadline"]["job_pool"]["value"]
        self.job_second_pool = config["deadline"]["job_second_pool"]["value"]
        self.job_group = config["deadline"]["job_group"]["value"]             
                        
        # denoise_name
        self.primary_name = 'primary'
        self.ml_name = 'ML'
        self.lpe_name = 'LPE'                              
                     
        # setup ui
        self.init_ui()
        self.btn_setup()
        self.setup_ui()        
        self.show()
        
        
    def init_ui(self):
        # main ui
        self.widget = body_widget.Ui_Form()
        self.widget.setupUi(self)
        # deadline options
        self.setting_widget = SettingWidget()
        self.widget.setting_layout.addWidget(self.setting_widget)
        
        
    def btn_setup(self):
        self.widget.local_button.clicked.connect(partial(self.set_redner, 'local'))
        self.widget.fram_button.clicked.connect(partial(self.set_redner, 'farm'))                    
        self.widget.deadline_checkbox.stateChanged.connect(self.get_deadline_options)
        self.widget.frame_checkbox.stateChanged.connect(self.active_set_frame)                             
        self.setting_widget.ui.delayed_checkBox.stateChanged.connect(self.active_stateChanged_delayed)             
        self.widget.stop_button.clicked.connect(self._stopProgress)          
        
        
    def get_user_dict(self):
        '''
        ww api에서 유저 정보 가져오기
        '''
        user_id = self.user_id = os.environ['USER']        
        
        try:
            for i in self.ww.get_user_info():
                if i['sg_ww_id'] == user_id:
                    user_dict = i                    
        except:
            user_dict = {}
            user_dict['sg_ww_id'] = str(user_id)
            user_dict['name'] = 'unknown'

        return user_dict


    def setup_ui(self):           
        #add tiems
        items = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7']
        self.widget.strength_combobox.addItems(items)
        text = '../RenderLayer/Denoise'
        self.widget.denoise_path_lineedit.setText(text)
        # ui set
        self.widget.primary_checkbox.setText(self.primary_name)
        self.widget.primary_checkbox.setChecked(True)        
        self.widget.ml_checkbox.setText(self.ml_name)
        self.widget.lpe_checkbox.setChecked(True)        
        self.widget.lpe_checkbox.setText(self.lpe_name)               
        self.widget.ml_checkbox.setChecked(True)        
        self.widget.local_progressbar.setValue(0)
        self.widget.stop_button.hide()        
        self.setting_widget.ui.frame_per_task_lineEdit.setReadOnly(True)        
        self.setting_widget.ui.frame_per_task_lineEdit.setText(' ')                
        # job setting 
        self.reload_comboBox(self.setting_widget.ui.pool_comboBox, self.job_pool)
        self.reload_comboBox(self.setting_widget.ui.secondary_pool_comboBox, self.job_second_pool)
        self.reload_comboBox(self.setting_widget.ui.group_comboBox, self.job_group)
        self.setting_widget.ui.machine_limit_lineEdit.setText('3')
        self.setting_widget.ui.delayed_dateTimeEdit.setDateTime(datetime.now())        
        # actions
        self.active_stateChanged_delayed()         
        self.active_set_frame()
        self.get_deadline_options()                  
        # 데드라인 잡 옵션 잠금
        self.widget.deadline_checkbox.hide()
        

    def reload_comboBox(self, comboBox, item_list):
        '''
        데드라인 잡 옵션 추가
        '''
        comboBox.clear()
        for _item in item_list:
            comboBox.addItem(_item)
            
            
    def active_stateChanged_delayed(self):
        '''
        데드라인 잡 딜레이 버튼 커넥트
        '''
        if self.setting_widget.ui.delayed_checkBox.isChecked():
            self.setting_widget.ui.delayed_dateTimeEdit.setEnabled(True)
        else:
            self.setting_widget.ui.delayed_dateTimeEdit.setEnabled(False)         
            
            
    def get_delayed_datetime(self):
        '''
        데드라인 잡 현재 시간 추가    
        '''
        if self.setting_widget.ui.delayed_checkBox.isChecked():
            delayed_datetime = self.setting_widget.ui.delayed_dateTimeEdit.dateTime()
            return delayed_datetime.toString("dd/MM/yyyy HH:mm")
        else:
            return            
            
            
    def active_set_frame(self):
        '''
        프레임 설정 커넥트
        '''
        if self.widget.frame_checkbox.isChecked():
            self.widget.start_label.show()
            self.widget.start_lineedit.show()
            self.widget.end_label.show()
            self.widget.end_lineedit.show()
        else:
            self.widget.start_label.hide()
            self.widget.start_lineedit.hide()
            self.widget.end_label.hide()
            self.widget.end_lineedit.hide()

            self.widget.start_lineedit.setText('')        
            self.widget.end_lineedit.setText('')              
            
            
    def get_deadline_options(self):
        '''
        데드라인 잡 옵션이 열려 있을 때, 사이즈 조절
        '''
        state = self.widget.deadline_checkbox.isChecked()
        
        if state:
            width, height = 1100, 420           
            self.setting_widget.ui.groupBox.show()            
            self.setting_widget.ui.memo_textEdit.show()            
            self.setting_widget.ui.label_27.show()            
        else:
            width, height = 720, 220        
            self.setting_widget.ui.groupBox.hide()            
            self.setting_widget.ui.memo_textEdit.hide()            
            self.setting_widget.ui.label_27.hide()                        
            
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)       
                                                                                    
                     
    def set_redner(self, render_type):
        '''
        render 버튼을 눌렀을 때, 정보를 취합하는 공간
        '''
        #
        path = self.widget.denoise_path_lineedit.text()
        strength = self.widget.strength_combobox.currentText()                 
        frame_check = self.widget.frame_checkbox.isChecked()          
        start_frame = self.widget.start_lineedit.text()        
        end_frame = self.widget.end_lineedit.text()       
        prefix =  self.widget.name_prefix_lineedit.text()
                
        # make dict
        self.denoise_dict = make_dict.DenoiseDict(path, self.primary_name, self.ml_name, self.lpe_name)
        # add dict items                                                                        
        self.denoise_dict.check_fixed_frame(frame_check, start_frame, end_frame)        
        self.denoise_dict.get_strength(strength)                
        self.denoise_dict.set_order(self.widget.primary_checkbox, prefix)
        self.denoise_dict.set_order(self.widget.ml_checkbox, prefix)
        self.denoise_dict.set_order(self.widget.lpe_checkbox, prefix)                
        
        #
        if self.denoise_dict.data['order']:
            if render_type == 'local':
                # local thread
                self.progress_task = LocalThread()
                self.progress_task.get_data(self.denoise_dict.data)
                self.progress_task.TASK_FINISHED.connect(self._onFinished)
                self.progress_task.PROGRESS_UPDATED.connect(self._updateProgress)                
                # LocalThread 실행                   
                self._onStart()                          
            else: # to farm
                # project
                self.current_path = self.denoise_dict.data['denoise_path'] 
                self.project_dict = self.ww.parse.parse_context(self.current_path)        
                version = self.ww.parse.parse_version_number(self.current_path)
                self.project_dict.update({'version' : version})       
                # user
                self.user_id = self.uesr_dict['sg_ww_id']
                self.user_name = self.uesr_dict['name']                                
                # farm setting
                self.pool_name = self.setting_widget.ui.pool_comboBox.currentText()
                self.second_pool_name = self.setting_widget.ui.secondary_pool_comboBox.currentText()
                self.group_name = self.setting_widget.ui.group_comboBox.currentText()
                self.priority = self.setting_widget.ui.priority_lineEdit.text()
                self.framePerTask = self.setting_widget.ui.frame_per_task_lineEdit.text()
                self.machine_limit = self.setting_widget.ui.machine_limit_lineEdit.text()
                self.delayed = self.get_delayed_datetime()
                self.memo = self.setting_widget.ui.memo_textEdit.toPlainText()
                self.step = 1
                                                                
                wDeadline = submit.Submit(
                    self.current_path, 
                    self.project_dict,
                    self.denoise_dict.data, 
                    self.uesr_dict,
                    self.pool_name, 
                    self.second_pool_name, 
                    self.group_name, 
                    self.priority, 
                    self.framePerTask, 
                    self.machine_limit,
                    self.delayed,
                    self.step,
                    self.memo
                    )                
                wDeadline.submit()
                          
                          
    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_L:
            if self.widget.deadline_checkbox.isHidden():
                self.widget.deadline_checkbox.show()
            else:
                self.widget.deadline_checkbox.hide()     


    def _onStart(self):        
        # ui option
        self.widget.local_button.setEnabled(False)
        self.widget.stop_button.show()       
        self.widget.fram_button.hide()                        
        
        # LocalThread
        self.issue_info = None                
        self.progress_task.start()        
        self.widget.local_progressbar.setRange(0, 100)


    def _stopProgress(self):
        self.progress_task.stop()
        self._setDefault()        
        
        self.issue_info = '로컬 렌더를 멈췄습니다.'
        
        
    def _updateProgress(self, value):
        self.widget.local_progressbar.setValue(value)
        

    def _setDefault(self):
        self.widget.local_button.setEnabled(True)
        self.widget.stop_button.hide()        
        self.widget.fram_button.show()            
        self.widget.local_progressbar.setValue(0)      
                      
                    
    def _onFinished(self):
        self._setDefault()
                           
        if self.issue_info:
            QMessageBox.warning(self, 'Warning', self.issue_info)                         
        else:
            QMessageBox.information(self, 'Done', '정상적으로 완료되었습니다.')                                   
        
                
#
# LocalThread  ==============================================================
#
               
        
class LocalThread(QtCore.QThread):
    TASK_FINISHED = Signal()
    PROGRESS_UPDATED = Signal(int)    
    STATUS = ''
    
    _stop_flag = False
    
    
    def stop(self):
        self._stop_flag = True    
    
    
    def run(self):                 
        # 레인지 구하기               
        start, end = map(int, self.fixed_frame.split('-'))
        total_commands = len(range(start, end+1)) * len(self.order.keys())

        index = 1
        for key, value in self.order.items()[::-1]:           
            for num in range(start, end + 1):
                if self._stop_flag:
                    break                                
                # data
                str_num = '{}-{}'.format(num, num)
                title_name = value['denoise']['name']
                out_path = value['denoise']['out_path']
                out_dir = value['denoise']['out_dir']
                
                # denose args
                denoise_cmd =  ['python'] 
                denoise_cmd.append(self.convert_path)
                denoise_cmd.append(title_name)
                denoise_cmd.append(self.denoise_path)
                denoise_cmd.append(self.total_frame)
                denoise_cmd.append(self.variance_path)
                denoise_cmd.append(out_path)
                denoise_cmd.append(out_dir)
                denoise_cmd.append(self.strength)
                denoise_cmd.append(str_num)
                denoise_cmd.append(out_dir)                                                
                                                                
                rename_cmd = []
                if value['rename']:       
                    old_name =  value['rename']['old']
                    new_name = value['rename']['new']                                             
                    # rename args                    
                    rename_cmd = [' ; ' 'python']                                                 
                    rename_cmd.append(self.rename_path)
                    rename_cmd.append(out_dir)
                    rename_cmd.append(old_name)
                    rename_cmd.append(new_name)
                    rename_cmd.append(str_num)

                # command
                cmds = denoise_cmd + rename_cmd
                cmd = ' '.join(cmds)
                LocalThread.STATUS = os.system(cmd)   

                current_progress = index * 100 / total_commands
                index += 1
                
                self.PROGRESS_UPDATED.emit(current_progress)

        self.TASK_FINISHED.emit()  


    def get_data(self, denoise_dict):
        # 
        _filepath = DenoiseToDeadline._filepath()
        rename_py = 'python/api/rename_to_fram.py'
        self.rename_path = os.path.join(_filepath, rename_py)        
        convert_py = 'python/api/convert_denoise_cmd.py'
        self.convert_path = os.path.join(_filepath, convert_py)
        
        if os.path.isfile(self.rename_path) and os.path.isfile(self.convert_path):
            self.denoise_path = denoise_dict['denoise_path']
            self.variance_path = denoise_dict['variance']
            self.strength = denoise_dict['flag']['strength']             

            self.order = denoise_dict['order']
            self.total_frame = denoise_dict['frame']['total_frame']                              
            self.fixed_frame = denoise_dict['frame']['fixed_frame']           
            if not self.fixed_frame:
                self.fixed_frame = self.total_frame
                                                                                   
        else:
            printInfo = 'python 파일을 찾지 못했습니다.'
            QMessageBox.warning(None, 'Warning', printInfo)                 
            raise ValueError(printInfo)
                
        
        
        
        
        
        
        
        
        
        
        

