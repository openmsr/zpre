import matplotlib
import openmc
from materials import *

###############################################################################
#generate geometry plot of zpre (boron sleeves fully inserted)
###############################################################################

h5m_filepath = 'h5m_files/zpre.h5m'

# materials
mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                         helium,scintillator,insulation,bepo,lindsay,gold,
                         aluminum,dt,fuel,boron])
mats.export_to_xml()

dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

#plotting geometry
plots = openmc.Plots()

x_width = 250
y_width = 250
res = 750

#xy plot
p1 = openmc.Plot()
#p1.origin=[0,0,100]
p1.width = (x_width,y_width)
p1.pixels = (res,res)
p1.color_by = 'material'

#xz plot
p2 = openmc.Plot()
#p2.origin=[0,0,100]
p2.basis = 'xz'
p2.width = (x_width,y_width)
p2.pixels = (res,res)
p2.color_by = 'material'

p3 = openmc.Plot()
#p3.origin=[0,0,100]
p3.basis = 'yz'
p3.width = (x_width,y_width)
p3.pixels = (res,res)
p3.color_by = 'material'

plots.append(p1)
plots.append(p2)
plots.append(p3)
plots.export_to_xml()

openmc.plot_geometry()
