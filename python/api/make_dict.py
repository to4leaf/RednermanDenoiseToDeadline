# -*- coding: utf-8 -*-
import os
import re

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class DenoiseDict():
    def __init__(self, path, primary_name, ml_name, lpe_name):
        # make dict
        self.data = {}    
        self.data['order'] = {}                        
        self.data['frame'] = {'total_frame' : '', 'fixed_frame' : '' }        
        
        # get used name
        self.primary_name = primary_name
        self.ml_name = ml_name
        self.lpe_name = lpe_name
        
        # name prefix
        self._var = '.var'
        self._variance = '.variance'
        self._filtered = '.filtered'
        
        # set default 
        self.get_path(path)
        self.get_frame()
        # 디노이즈 패스가 없는 파일은 있는 파일을 바라보게 셋팅해야함.
        # ex) primary.variance.1001.exr ML.var.1001.exr
        variance = self.get_formating_name(self.primary_name, self._var, self._variance)      
        self.data['variance'] = variance        

            
    def get_path(self, path):
        '''
        기본 경로를 가져오는데, 디노이즈 경로를 가져오는데 약간 예외적인 경우도 찾아주게 셋팅
        denoise_path : (str)/show/jung/seq/EP11/EP11_S001_0050/lgt/dev/precomp/r1/v000/crowd_01_all/Denoise
        '''
        split_edit_path = path.split('/')
        check_name_list = [self.primary_name+self._variance, 
                                 self.primary_name+self._var,
                                 self.ml_name+self._var,
                                 self.lpe_name+self._var
                                 ]        

        denoise_path = None        
        if os.path.isdir(path):
            # 추구하는 기본 경로
            if split_edit_path[-1] == 'Denoise':
                denoise_path = path
            # 예외로 찾기
            elif split_edit_path[-1] in check_name_list and split_edit_path[-2] == 'Denoise':
                denoise_path = os.path.dirname(path)
        else:
            # 예외로 찾기
            if split_edit_path[-2] in check_name_list and split_edit_path[-3] == 'Denoise':
                denoise_path = os.path.dirname(os.path.dirname(path))

        if denoise_path == None:
            printInfo = 'Denoise Path를 확인해주세요.'
            QMessageBox.warning(None, 'Warning', printInfo)                 
            raise ValueError(printInfo)
        else:
            self.data['denoise_path'] = str(denoise_path)

            
    def get_frame(self):
        '''
        denoise/primary 폴더 안에 있는 파일 탐색으로 프레임 계산
        total_frame : (str) 1001-1101
        '''
        primary_dir = os.path.join(self.data['denoise_path'], self.primary_name+self._var)
        if os.path.isdir(primary_dir):
            all_files = os.listdir(primary_dir)
            filtered_files = [f for f in all_files if f.startswith(self.primary_name+self._variance)]
            seq_num = [int(re.search(r'\d+', f).group()) for f in filtered_files]
            seq_num.sort()
            
            self.data['frame']['total_frame'] = str(seq_num[0])+'-'+str(seq_num[-1])
                
        else:
            printInfo = 'primary 관련 경로를 확인해주세요.'
            QMessageBox.warning(None, 'Warning', printInfo)                 
            raise ValueError(printInfo)            
            
            
    def get_strength(self, strength):                
        '''
        flag : (str) 0.2
        '''                                                                          
        if strength:            
            self.data['flag'] = {'strength' : str(strength)}
        else:
            printInfo = 'flag를 가져오지 못했습니다.'
            QMessageBox.warning(None, 'Warning', printInfo)                 
            raise ValueError(printInfo)

            
                        
    def check_fixed_frame(self, frame_check, start, end):
        '''
        전체 렌더가 아닌 특정 구간만 렌더하고 싶을 때, 프레임 설정
        전체 리스트에서 해당 구간이 아닌 부분을 지우는 방식
        '''
        if frame_check:
            old_start, old_end = self.data['frame']['total_frame'].split('-')    
            if start and end:
                # 시작 프레임 체크
                if int(start) < int(old_start):
                    printInfo = '시작 프레임이 기존 프레임보다 작습니다.'
                    QMessageBox.warning(None, 'Warning', printInfo)                 
                    raise ValueError(printInfo)                
                # 마지막 프레임 체크
                if int(end) > int(old_end):
                    printInfo = '마지막 프레임이 기존 프레임보다 큽니다.'
                    QMessageBox.warning(None, 'Warning', printInfo)                 
                    raise ValueError(printInfo)               
                    
                if int(start) > int(end): 
                    printInfo = '프레임 범위가 이상합니다.'
                    QMessageBox.warning(None, 'Warning', printInfo)                 
                    raise ValueError(printInfo)                  

                self.data['frame']['fixed_frame'] = str(start + '-' + end)
                    
            else:
                printInfo = 'Start, End에 프레임을 추가해주세요.'
                QMessageBox.warning(None, 'Warning', printInfo)                 
                raise ValueError(printInfo)
                        
                        
    def set_order(self, checkbox, prefix):
        '''
        order 리스트 만들어 주기
        '''
        if checkbox.isChecked():        
            check_name = checkbox.text()                               
            self.data['order'].update({str(check_name) : {}})
            self.get_denoise_items(check_name, prefix)
            self.rename_config(check_name)

                        
    def get_denoise_items(self, order, prefix):
        '''
        out_dir : (str) /show/jung/seq/EP11/EP11_S001_0050/lgt/dev/precomp/r1/v000/crowd_01_all/Filtered
        name : (str) primary_s02.filtered
        out_path : (str) {path}/primary.var/primary.variance.{num}.exr
        '''
        self.data['order'][order]['denoise'] = {}        

        var_name = order + self._var
        filtered_name = order + self._filtered
        if prefix:
            var_name = order + '_' + prefix + self._var
            filtered_name = order + '_' + prefix + self._filtered            
        
        formating_name = self.get_formating_name(order, self._var, self._variance)                  
        if not order in 'primary': 
            formating_name = self.get_formating_name(order, self._var, self._var)                               

        filtered_path = self.data['denoise_path'].replace('Denoise', 'Filtered')
        order_output_dir =  str(os.path.join(filtered_path, filtered_name))
        self.data['order'][order]['denoise']['out_dir'] = order_output_dir
        self.data['order'][order]['denoise']['name'] = str(var_name)
        self.data['order'][order]['denoise']['out_path'] = formating_name            
        
        
    def rename_config(self, order):
        '''
        리네임을 할 때 포매팅 네이밍 구성
        old : (str){path}/ML.var/ML.var_filtered.{num}.exr
        new : (str){path}/ML.var/ML.filtered.{num}.exr                
        '''
        self.data['order'][order]['rename'] = {}        
        if not order in 'primary': 
            o_name = self.get_formating_name('', '', order+self._var+'_filtered')
            n_name = self.get_formating_name('', '', order+'.filtered')

            self.data['order'][order]['rename']['old'] = o_name                
            self.data['order'][order]['rename']['new'] = n_name         
                        
                        
    def get_formating_name(self, order, var, variance):
        '''
        포매팅 네이밍 구성
        '''
        path = '{path}'
        dirname = '{}{}'.format(order, var)
        basename = '{}{}.{}.exr'.format(order, variance, '{num}')
        
        return os.path.join(path, dirname, basename)   
                        
                        

