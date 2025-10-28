# -*- coding: utf-8 -*-
import os
import sys

# PyYAML, ww_api, shotgrid_api3, PySide2, deadline_common
sys.path.append('/westworld/inhouse/tool/rez-packages/PyYAML/3.10/python')
sys.path.append('/westworld/inhouse/tool/rez-packages/ww_api/python')
sys.path.append('/westworld/inhouse/tool/rez-packages/shotgrid_api3/3.3.4')
sys.path.append("/westworld/inhouse/dept_pipeline/rez-packages/dcc/deadline_common/1.0/python")


def _filepath():
    path = os.path.abspath(__file__ +'/../')
    return path

