from PySide6.QtCore import QMutex, QWaitCondition, QThread, Signal
import numpy as np
from initial.eam_force import eam_force
from output.read_datafile import read_datafile
from initial.integrate import integrate
from initial.T_conduct import NEMD, compute_result
from initial.vacf_pdos import find_pdos
from initial.create_eam import create_eam
from initial.initialize_system import System
import copy
class Work(QThread):
    signal = Signal(object)
    def __init__(self, element1, element2, element3, filepath, temperature0, iterate, ensemble_name, ensemble_name_1, heat, iterate_1, x):
        super(Work, self).__init__()
        if element2 != '' and element3 != '':
            create_eam([element2, element3])
            self.filename_potential = 'data/' + element2 + element3 + '.eam.alloy'
        if element1 != '':
            create_eam([element1])
            self.filename_potential = 'data/' + element1 + '.eam.alloy'
        self.temperature0 = temperature0
        self.iterate = iterate
        self.ensemble_name = ensemble_name
        self.ensemble_name_1 = ensemble_name_1
        self.Tot_data = read_datafile(filepath)
        self.heat = heat
        self.iterate_1 = iterate_1
        self.Tot_data_initial = copy.deepcopy(self.Tot_data)
        self.x = x

        self.is_paused = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()
    
    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        self.cond.wakeAll()
    
    def run(self):
        self.T_axis = []
        self.Pe_axis = []
        self.Time_axis = []
        System_create = System(self.Tot_data, temperature0=self.temperature0)
        self.timestep = System_create.time_step
        self.velocity = System_create.initialize()
        for i in range(self.iterate):
            self.mutex.lock()
            if self.is_paused == True:
                self.cond.wait(self.mutex)
            if self.is_paused == False:
                if i == 0:
                    self.Temperature = self.temperature0
                EAM = eam_force(self.filename_potential, self.Tot_data)
                EAM.read_eam()
                EAM.compute_eam()
                [self.Temperature, self.Tot_data, self.velocity, EAM] = integrate(self.Tot_data, EAM, self.velocity, self.ensemble_name, self.Temperature, self.temperature0, 1, self.timestep)
                self.T_axis.append(self.Temperature)
                self.Pe_axis.append(EAM.pe)
                self.Time_axis.append(i * self.timestep)
            self.mutex.unlock()
        for i in range(self.iterate_1):
            self.mutex.lock()
            if self.is_paused == True:
                self.cond.wait(self.mutex)
            if self.is_paused == False:
                self.Tot_data, self.velocity, EAM, self.T_chunk, self.Temperature, self.dT_dx, self.heat, self.x_chunk = NEMD(self.Tot_data, self.velocity, EAM, self.timestep, self.temperature0, self.ensemble_name_1, self.heat, 1, self.x)
                self.temperature0 = self.Temperature
            self.mutex.unlock()
        self.t_conductivity = compute_result(self.Tot_data_initial, self.dT_dx, self.heat)
        self.Thermal_conductivity = [self.T_chunk, self.x_chunk, self.t_conductivity]
        self.omega = np.arange(1, 380.5, 0.5)
        [self.vacf_output, self.pdos] = find_pdos(self.velocity, 100, omega=self.omega)
        self.signal.emit([self.Tot_data, self.T_axis, self.Pe_axis, self.Time_axis, self.Thermal_conductivity])
