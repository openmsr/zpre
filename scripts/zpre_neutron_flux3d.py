import matplotlib.pyplot as plt
import openmc
from materials import *
import numpy as np

###############################################################################
#create .png file of neutron flux (boron sleeves fully inserted)
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

#materials
mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                         helium,scintillator,insulation,bepo,lindsay,gold,
                         aluminum,dt,fuel,boron])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 5000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#tallies
tallies = openmc.Tallies()


mesh3d = openmc.RegularMesh()
mesh3d.dimension = [300,300,300]
mesh3d.lower_left = [-125,-125,-125+100]
mesh3d.upper_right = [125,125,125+100]
mesh3d_filter=openmc.MeshFilter(mesh3d)

tally3d = openmc.Tally(name='flux3d')
tally3d.filters = [mesh3d_filter]
tally3d.scores=['flux','fission']
tallies.append(tally3d)

tallies.export_to_xml()
