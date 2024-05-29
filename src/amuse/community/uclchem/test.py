from interface import Uclchem
from amuse.datamodel import Particles
from amuse.units import units
chem = Uclchem()
particles = Particles(1)
particles.number_density = 1.0 | units.cm**-3
particles.temperature = 20 | units.K
particles.ionrate = 10**-16 | units.s**-1
print(particles)
chem.particles.add_particle(particles)
print(chem.particles.number_density)
chem.evolve_model()
print(chem.particles.abundances)
#print(chem.sim_cloud(outSpeciesIn=species, dictionary=dict))
#print(test)