from interface import Uclchem
from amuse.datamodel import Particles
from amuse.units import units
#species='H H2'
#dict = "{'outspecies': 2}"
chem = Uclchem()
particles = Particles(1)
particles.temperature = 20 | units.K
chem.particles.add_particles(particles)
chem.evolve_model()
#print(test)