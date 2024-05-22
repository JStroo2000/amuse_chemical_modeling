from amuse.community.interface.chem import ChemicalModelingInterface
from amuse.community.interface.chem import ChemicalModeling
from amuse.community.interface import common
from amuse.community import *

class UclchemInterface(CodeInterface):
    def __init__(self, mode = 'cpu', **options):
        CodeInterface.__init__(
            self,
            name_of_the_worker='uclchem_worker',
            **options
        )
    

    @remote_function(can_handle_array=True)
    def sim_cloud(outSpeciesIn='s', dictionary='s'):
        
        returns (abundance='d')

    def _make_dictionary(self):
        return "{'outspecies': 2, 'initialTemp': {}}".format(self.particles.temperature)
    
    def evolve_model(self):
        #dictionary  = self._make_dictionary(self)
        abundance = self.sim_cloud('H H2', "{'outspecies': 2, 'initialTemp': {}}".format(self.particles.temperature))
        print(abundance)

    

class Uclchem(ChemicalModeling):
    def __init__(self, convert_nbody=None, **options):
        legacy_interface = UclchemInterface(**options)

        ChemicalModeling.__init__(self,legacy_interface)

    def define_particle_sets(self, object):
        object.define_inmemory_set('particles')
    
    def define_methods(self, handler):
        common.CommonCode.define_methods(self, handler)
        handler.add_method(
            'sim_cloud',
            (handler.NO_UNIT, handler.NO_UNIT),
            (handler.NO_UNIT, handler.ERROR_CODE)
        )
        handler.add_method(
            'evolve_model',
            (),
            ()
        )
