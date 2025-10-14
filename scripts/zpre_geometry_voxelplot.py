import matplotlib
import openmc
from materials import *

###############################################################################
#generate geometry plot of zpre (boron sleeves fully inserted)
###############################################################################

# geometry
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
mats.export_to_xml()

#plotting geometry
plots = openmc.Plots()

x_width = 250
y_width = 250
z_width = 250
res = 1000

#xy plot
p1 = openmc.Plot()
p1.origin=[0,0,100]
p1.type='voxel'
p1.filename='voxelplot'
p1.width=(x_width,y_width,z_width)
p1.pixels=(300,300,300)
p1.color_by = 'material'

plots.append(p1)
plots.export_to_xml()

openmc.plot_geometry()
