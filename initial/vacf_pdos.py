
import numpy as np

### set up some parameters related to the MD simulation
# N = 1728  # number of atoms
# Nc = 2000  # number of correlation steps (a larger number gives a finer resolution)
# dt = 0.0005  # time interval in units of ps (its inverse is roughly the maximum frequency attainable)
# omega = np.arange(1, 380.5, 0.5)  # angular frequency in units of THz
# nu = omega / 2 / np.pi;  # omega = 2 * pi * nu, while nu is the frequency range
# Nf = Nc * 10  # The calculation numbers
# num_frame = Nf  # Frame numbers equals to calculation numbers
# fileName = "DUT49_charge_voutput_all.lammpstrj"  # Read the dump file


def find_pdos(v_all, Nc, dt = 0.001, omega = np.arange(1, 380.5, 0.5)):  # Calculate the vacf from velocity data
    Nf = v_all.shape[0]  # number of frames
    M = Nf - Nc  # number of time origins for time average
    vacf = np.zeros(Nc)  # the velocity autocorrelation function (VACF)
    for nc in range(Nc):  # loop over the correlation steps
        # ratio = (nc + 1) / Nc * 100
        # print("Calculate PDOS Progress %s%%" % ratio)
        for m in range(M + 1):  # loop over the time origins
            delta = np.sum(v_all[m + 0] * v_all[m + nc])
            # print(delta)
            vacf[nc] = vacf[nc] + delta
    vacf = vacf / vacf[0]  # normalize the VACF
    vacf_output = vacf  # copy the VACF before modifying it
    vacf = vacf * (np.cos(np.pi * np.arange(Nc) / Nc) + 1) * 0.5  # window function
    vacf = vacf * np.append(np.ones(1), 2 * np.ones(Nc - 1)) / np.pi  # C(t) = C(-t)
    pdos = np.zeros(len(omega))  # the phonon density of states (PDOS)
    for n in range(len(omega)):  # Discrete cosine transform
        pdos[n] = dt * sum(vacf * np.cos(omega[n] * np.arange(Nc) * dt))
    return (vacf_output, pdos)

if __name__ == '__main__':
    import numpy as np
    from initial.read_data import ReadLmpData
    import sys
    from eam_force import compute_eam
    from initial.initialize_system import System
    from integrate import integrate
    import matplotlib.pyplot as plt
    TotData = ReadLmpData('Cu1.lmp')
    TotData.run_read()
    System = System(total_data=TotData)
    velocity = System.initialize()
    Tot_pe, force = compute_eam(filename='Cu.eam.alloy', TotData=TotData)
    steps = 200
    v_all = np.zeros((steps, TotData.atom_num, 3))
    for j in range(steps):
        [Temperature, TotData, velocity, pe, force] = integrate(TotData, 'Cu.eam.alloy', velocity, force, 'nvt', 300)
    for i in range(steps):
        v_all[i] = velocity
        [Temperature, TotData, velocity, pe, force] = integrate(TotData, 'Cu.eam.alloy', velocity, force, 'nve', 300)

    vcaf, pdos = find_pdos(v_all, 100, omega=np.arange(1, 380.5, 0.5))
    nu = np.arange(1, 380.5, 0.5) / 2 / np.pi
    t = np.arange(100) * 0.001
    print(pdos)
    plt.subplot(1,2,1)
    plt.plot(nu[40:], pdos[40:])
    plt.subplot(1,2,2)
    plt.plot(t, vcaf)
    plt.show()