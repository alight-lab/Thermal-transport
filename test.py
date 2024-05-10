from PyQt5.QtWidgets import QApplication
from ovito.io import import_file
import matplotlib.pyplot as plt

# 创建一个QApplication实例
# app = QApplication([])

# # 加载.lmp文件
# pipeline = import_file('lattice_0.lmp')

# # 计算并获取数据
# data = pipeline.compute()

# # 提取粒子位置数据
# positions = data.particles['Position']

# # 使用matplotlib进行绘图
# plt.scatter(positions[:,0], positions[:,1])
# plt.show()