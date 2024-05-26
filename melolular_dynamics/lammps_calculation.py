from PySide6.QtCore import QMutex, QWaitCondition, QThread, Signal
import numpy as np
import subprocess
from lammps import PyLammps
from output.renew import renew
from initial.Defect_Generation import defect

class Work(QThread):
    signal = Signal(object)
    signal_2 = Signal(object)
    py_lammps: PyLammps
    def __init__(self, element1, element2, element3, filepath, temperature0, temperature_set, iterate, ensemble_name, ensemble_name_1, heat, iterate_1, defect_num, x):
        print(filepath)
        super(Work, self).__init__()
        self.element1 = element1
        self.element2 = element2
        self.element3 = element3
        self.temperature0 = temperature0
        self.temperature_set = temperature_set
        self.iterate_time = iterate
        self.ensemble_name = ensemble_name
        self.ensemble_name_heat = ensemble_name_1
        self.heat = heat
        self.iterate_time_heat = iterate_1
        self.defect_num = defect_num
        self.filepath = filepath
        self.x = x
        self.py_lammps = PyLammps()
        with open(self.filepath, 'r') as f:
            line = f.readline()
            while line.find('xlo') == -1:
                line = f.readline()
        data = line.split()
        self.lattice_x_max_1 = data[1]

        self.is_paused = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        self.cond.wakeAll()

    def run(self):
        Total_data = defect("data/lattice.lmp", self.defect_num)
        renew(Total_data)
        if self.element2 == '':
            line_write = ['variable '+'init_tempareture'+' equal '+ str(self.temperature0),
            'variable '+'setted_tempareture'+' equal '+ str(self.temperature_set),
            'variable '+'lattice_ensemble'+' string '+ str(self.ensemble_name),
            'variable '+'lattice_steps'+' equal '+ str(self.iterate_time/0.001),
            'variable '+'heat_flux'+' equal '+ str(self.heat),
            'variable '+'heat_ensemble'+' string '+ str(self.ensemble_name_heat),
            'variable '+'sim_steps'+' equal '+ str(self.iterate_time_heat/0.001),
            'variable '+'vacancy'+' equal '+ str(self.defect_num),
            'variable '+'type_1'+' string '+ str(self.element1),
            'variable '+'potential_name'+' string '+ 'data/' + self.element1 + '.eam.alloy',
            'variable '+'lattice_x_max_1'+' equal '+ str(self.lattice_x_max_1)]
            for i in range(len(line_write)):
                self.py_lammps.command(line_write[i])
            with open('melolular_dynamics/in/in.lattice', 'r', encoding='UTF-8') as f:
                lines = f.readlines()
            for line in lines:
                if self.is_paused == False:
                    self.py_lammps.command(line)
                if self.is_paused == True:
                    self.signal_2.emit('暂停')
                    self.cond.wait(self.mutex)
        else:
            line_write = ['variable '+'init_tempareture'+' equal '+ str(self.temperature0),
            'variable '+'setted_tempareture'+' equal '+ str(self.temperature_set),
            'variable '+'lattice_ensemble'+' string '+ str(self.ensemble_name),
            'variable '+'lattice_steps'+' equal '+ str(self.iterate_time/0.001),
            'variable '+'heat_flux'+' equal '+ str(self.heat),
            'variable '+'heat_ensemble'+' string '+ str(self.ensemble_name_heat),
            'variable '+'sim_steps'+' equal '+ str(self.iterate_time_heat/0.001),
            'variable '+'vacancy'+' equal '+ str(self.defect_num),
            'variable '+'type_1'+' string '+ str(self.element2),
            'variable '+'type_2'+' string '+ str(self.element3),
            'variable '+'potential_name'+' string '+ 'data/' + self.element2 + self.element3 + '.eam.alloy',
            'variable '+'lattice_x_max_1'+' equal '+ str(self.lattice_x_max_1),
            'variable '+'diff_x'+' equal '+ str(self.x)]
            print(line_write[-1])
            for i in range(len(line_write)):
                self.py_lammps.command(line_write[i])
            with open('melolular_dynamics/in/in.lattice_2', 'r', encoding='UTF-8') as f:
                lines = f.readlines()
            for line in lines:
                if self.is_paused == False:
                    self.py_lammps.command(line)
                if self.is_paused == True:
                    self.signal_2.emit('暂停')
                    self.cond.wait(self.mutex)
        self.signal.emit('计算完毕')


if __name__ == '__main__':
    t = Work('Cu', '', '', 'data/lattice.lmp', 200, 300, 1, 'nvt', 'nve', 10, 1, 100)
    t.run()