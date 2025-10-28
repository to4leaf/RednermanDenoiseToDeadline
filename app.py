# -*- coding: utf-8 -*-
import os
import sys
import yaml
import logging
logging.basicConfig()

#init실행
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import DenoiseToDeadline
reload(DenoiseToDeadline)

file_path = DenoiseToDeadline._filepath()


with open(file_path + '/resources/info.yaml', 'r') as f:
    _config = yaml.safe_load(f)
    config = _config["configuration"]


def main():
    from python import dialog
    reload(dialog)

    global denoise_app
    denoise_app = dialog.DenoiseApp(config)


if __name__ == "__main__":
    sys.path.append('/westworld/inhouse/tool/rez-packages/PySide2/5.13/platform-linux/arch-x86_64/lib64/python2.7/site-packages')
    from PySide2 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    main() # 실행
    sys.exit(app.exec_())





