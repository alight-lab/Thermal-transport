import os
os.environ['OVITO_GUI_MODE'] = '1'

from GUI.main_window import MainWindow
from output import render_3d

from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

render_3d.insert_widget(window.painting_zoom)

sys.exit(app.exec())
#体系区域温度图像加上柱状图
#区域温度可视化
#colorbar单位
#单晶及多晶声子态密度
#热导率结果计算
#热流单位修改
#数据导出
#帮助手册
#推荐参数修改
#删无用的文件
#


