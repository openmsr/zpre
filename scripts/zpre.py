import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#k eigenvalue simulation on ZPRE (boron sleeves fully inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/zpre_simplified_4.h5m'

mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                         helium,scintillator,insulation,bepo,lindsay,gold,
                         aluminum,dt,fuel,boron])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 10000
#source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.])
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()
dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()


openmc.run()
