from PySide6.QtCore import QMutex, QWaitCondition, QThread, Signal
import numpy as np
from initial.eam_force import eam_force
from initial.integrate import integrate
from initial.T_conduct import NEMD, compute_result
from initial.vacf_pdos import find_pdos
from initial.create_eam import create_eam
from initial.initialize_system import System
from initial.Defect_Generation import defect
import copy
class Work(QThread):
    signal = Signal(object)
    signal_2 = Signal(object)
    signal_3 = Signal(object)
    def __init__(self, element1, element2, element3, filepath, temperature0, temperature_set, iterate, ensemble_name, ensemble_name_1, heat, iterate_1, x, defect_num):
        super(Work, self).__init__()
        if element2 != '' and element3 != '':
            create_eam([element2, element3])
            self.filename_potential = 'data/' + element2 + element3 + '.eam.alloy'
        if element1 != '':
            create_eam([element1])
            self.filename_potential = 'data/' + element1 + '.eam.alloy'
        self.temperature0 = temperature0
        self.temperature_set = temperature_set
        self.iterate = iterate
        self.ensemble_name = ensemble_name
        self.ensemble_name_1 = ensemble_name_1
        self.Tot_data = defect(filepath, defect_num)
        self.heat = heat
        self.iterate_1 = iterate_1
        self.Tot_data_initial = copy.deepcopy(self.Tot_data)
        self.x = x
        self.x_chunk = []
        self.T_chunk = []
        self.pdos = []
        self.omega = []

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
        
        self.temp = 1
        EAM = eam_force(self.filename_potential)
        EAM.read_eam()
        for i in range(self.iterate):
            self.mutex.lock()
            if self.is_paused == True:
                self.temp = 2
                self.signal_2.emit([self.Tot_data, self.temp])
                self.cond.wait(self.mutex)

            if self.is_paused == False:

                if i == 0:
                    self.Temperature = self.temperature0
                    time = 0
                EAM.compute_eam(self.Tot_data)
                [self.Temperature, self.Tot_data, self.velocity, EAM, time] = integrate(self.Tot_data, EAM, self.velocity, self.ensemble_name, self.Temperature, self.temperature_set, 1, self.timestep, time)
                self.T_axis.append(self.Temperature)
                self.Pe_axis.append(EAM.pe)
                self.Time_axis.append(i * self.timestep)
            self.mutex.unlock()
        
        self.temp = 1
        EAM = eam_force(self.filename_potential)
        EAM.read_eam()
        self.Tot_data = copy.deepcopy(self.Tot_data_initial)
        System_create = System(self.Tot_data, temperature0=self.temperature0)
        self.timestep = System_create.time_step
        self.velocity = System_create.initialize()
        for i in range(self.iterate_1):
            self.mutex.lock()
            if self.is_paused == True:
                self.temp = 2
                self.signal_3.emit([self.Tot_data, self.temp])
                self.cond.wait(self.mutex)
            if self.is_paused == False:
                if i == 0:
                    self.Temperature = self.temperature0
                EAM.compute_eam(self.Tot_data)
                [self.Tot_data, self.velocity, EAM, self.T_chunk, self.Temperature, self.dT_dx, self.heat, self.x_chunk] = NEMD(self.Tot_data, self.velocity, EAM, self.timestep, self.Temperature, self.ensemble_name_1, self.heat, 1, self.x)
                self.temperature0 = self.Temperature
            self.mutex.unlock()
        self.temp = 1
        self.t_conductivity = compute_result(self.Tot_data, self.dT_dx, self.heat)
        self.Thermal_conductivity = [self.T_chunk, self.x_chunk, self.t_conductivity]
        self.omega = np.arange(1, 380.5, 0.5)
        [self.vacf_output, self.pdos] = find_pdos(self.velocity, 100, omega=self.omega)
        self.signal.emit([self.Tot_data, self.T_axis, self.Pe_axis, self.Time_axis, self.Thermal_conductivity])
