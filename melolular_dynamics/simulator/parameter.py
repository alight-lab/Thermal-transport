from enum import Enum


class Structure(Enum):
    bcc = None
    fcc = None


class AtomParameter:
    def __init__(
            self,
            lattice_constant:   float,
            structure:          Structure,
            mass:               float
        ) -> None:
        self.lattice_constant = lattice_constant
        self.structure = structure
        self.mass = mass
        


class Ensemble(Enum):
    nvt = None
    nve = None


class AtomType(Enum):
    Cu = AtomParameter(3.61, Structure.fcc,  63.55)
    Ag = AtomParameter(4.09, Structure.fcc, 107.87)
    Au = AtomParameter(4.08, Structure.fcc, 196.97)
    Ni = AtomParameter(3.52, Structure.fcc,  58.69)
    Pd = AtomParameter(3.89, Structure.fcc, 106.42)
    Pt = AtomParameter(3.92, Structure.fcc, 195.08)
    Al = AtomParameter(4.05, Structure.fcc,  26.98)
    Pb = AtomParameter(4.95, Structure.fcc,  207.2)
    Fe = AtomParameter(2.87, Structure.bcc,  55.85)
    Mo = AtomParameter(3.15, Structure.bcc,  95.95)
    Ta = AtomParameter(3.30, Structure.bcc, 180.95)
    W  = AtomParameter(3.16, Structure.bcc, 183.84)
    Mg = AtomParameter(3.21, Structure.fcc,  24.31)
    Co = AtomParameter(3.54, Structure.fcc,  58.93)
    Ti = AtomParameter(3.32, Structure.fcc,  47.87)
    Cr = AtomParameter(2.88, Structure.bcc,  51.99)
    Zr = AtomParameter(3.23, Structure.bcc,  91.22)


class AtomTypeContainer:
    def __init__(
            self,
            atom_type: AtomType,
            num_x: int,
            num_y: int,
            num_z: int
        ):
        self.atom_type = atom_type
        self.num_x = num_x
        self.num_y = num_y
        self.num_z = num_z

        
    


class SystemVarContainer:
    init_tempareture:   float
    setted_tempareture: float
    lattice_ensemble:   Ensemble
    lattice_time:       float
    heat_flux:          float
    heat_fixs:          Ensemble
    sim_time:           float
    vacancy:            int

    def __init__(
            self,
            init_tempareture:   float,
            setted_tempareture: float,
            lattice_fixs:       Ensemble,
            lattice_time:       float,
            heat_flux:          float,
            heat_fixs:          Ensemble,
            sim_time:           float,
            vacancy:            int
        ):
        
        self.init_tempareture = init_tempareture
        setted_tempareture    = setted_tempareture
        self.lattice_ensemble = lattice_fixs
        self.lattice_time     = lattice_time
        self.heat_flux        = heat_flux
        self.heat_fixs        = heat_fixs
        self.sim_time         = sim_time
        self.vacancy          = vacancy


class Variable:
    atoms: list[AtomTypeContainer]
    system: SystemVarContainer

    def __init__(self, atoms:list[AtomTypeContainer], system: SystemVarContainer) -> None:
        self.atoms = atoms
        self.system = system
        self.commands = self.__into_cmds()

    def __into_cmds(self) -> list[str] :
        result = []
        num_type = 1
        for atom in self.atoms:
            result.append('variable '+'type_'+str(num_type)+' equal '+str(num_type)) # eg. type_1
            result.append('variable '+'type_'+str(num_type)+'_mass'+' equal '+str(atom.atom_type.value.mass)) # eg. type_1_mass
            result.append('variable '+'type_'+str(num_type)+'_lattice_constant'+' equal '+str(atom.atom_type.value.lattice_constant)) # eg. type_1_lattice_constant
            result.append('variable '+'type_'+str(num_type)+'_structure'+' string '+str(atom.atom_type.value.structure.name)) # eg. type_1_structure
            result.append('variable '+'type_'+str(num_type)+'_x'+' equal '+str(atom.num_x)) # eg. type_1_x
            result.append('variable '+'type_'+str(num_type)+'_y'+' equal '+str(atom.num_y)) # eg. type_1_y
            result.append('variable '+'type_'+str(num_type)+'_z'+' equal '+str(atom.num_z)) # eg. type_1_z
            num_type = num_type + 1

        result.append('variable '+'init_tempareture'+' equal '+ str(self.system.init_tempareture)) # init_tempareture
        result.append('variable '+'setted_tempareture'+' equal '+ str(self.system.setted_tempareture)) # setted_tempareture
        result.append('variable '+'lattice_ensemble'+' string '+ str(self.system.lattice_ensemble)) # lattice_fixs
        result.append('variable '+'lattice_time'+' equal '+ str(self.system.lattice_time)) # lattice_time
        result.append('variable '+'heat_flux'+' equal '+ str(self.system.heat_flux)) # heat_flux
        result.append('variable '+'heat_ensemble'+' string '+ str(self.system.heat_fixs)) # heat_fixs
        result.append('variable '+'sim_time'+' equal '+ str(self.system.sim_time)) # sim_time
        result.append('variable '+'vacancy'+' equal '+ str(self.system.vacancy)) # vacancy

        return result
    

if __name__ == '__main__':
    var = Variable(
        [AtomTypeContainer(
            AtomType.Ag,
            5,5,5
        ),
        AtomTypeContainer(
            AtomType.Cu,
            5,5,5
        )
        ],
        SystemVarContainer(
            200,Ensemble.nve,1,10,Ensemble.nvt,1,100
        )
    )

    print(var.commands)