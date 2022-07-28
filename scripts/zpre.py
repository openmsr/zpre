import matplotlib.pyplot as plt
import sys
sys.path.append('/opt/openmc/')
import openmc
from materials import *

###############################################################################
#k eigenvalue simulation on ZPRE (boron sleeves fully inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/zpre.h5m'
graveyard = openmc.Sphere(r=10000,boundary_type='vacuum')
cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True)
cad_cell = openmc.Cell(region=-graveyard,fill=cad_univ)
root=openmc.Universe()
root.add_cells([cad_cell])
geometry=openmc.Geometry(root)
geometry.export_to_xml()


# materials
mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                         helium,scintillator,insulation,bepo,lindsay,gold,
                         aluminum,dt,fuel,boron])
mats.cross_sections='/home/luke/openmc/nuclear_data/endfb80_hdf5/cross_sections.xml'
mats.export_to_xml()

# settings
settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
#source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.cross_sections='/opt/nuclear_data/endfb80_hdf5/cross_sections.xml'
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.])
settings.source = openmc.Source(space=source_area)
settings.max_lost_particles=1000
settings.export_to_xml()


openmc.run()
