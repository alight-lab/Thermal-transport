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
#体系模型分块单晶分20块、多晶每种材料分10块
#in文件x方向边界条件修改，热源热汇改成第2块和第19块
#体系区域温度图像加上柱状图
#colorbar单位
#使用for循环修改运行步数
#相对原子质量目前UI无法显示全，将相对原子质量保留到小数点后一位
