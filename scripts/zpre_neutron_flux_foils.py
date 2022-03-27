import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#create .png file of neutron flux (boron sleeves fully inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/zpre.h5m'

#materials
mats = openmc.Materials([salt,BeO,inconel,insulation,coolant,helium,stainless,boron,blanket,shield])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 5000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

dag_univ = openmc.DAGMCUniverse(h5m_filepath)
geom = openmc.Geometry(root=dag_univ)
geom.export_to_xml()

tallies = openmc.Tallies()

# foil 1
foil_tally_1 = openmc.Tally(name='foil_1')
foil_tally_1.scores = ['flux']
foil_tally_1.filters = [openmc.CellFilter(58)]
tallies.append(foil_tally_1)

# foil 2
foil_tally_2 = openmc.Tally(name='foil_2')
foil_tally_2.scores = ['flux']
foil_tally_2.filters = [openmc.CellFilter(126)]
tallies.append(foil_tally_2)

# foil 3
foil_tally_3 = openmc.Tally(name='foil_3')
foil_tally_3.scores = ['flux']
foil_tally_3.filters = [openmc.CellFilter(94)]
tallies.append(foil_tally_3)

# foil 4
foil_tally_4 = openmc.Tally(name='foil_4')
foil_tally_4.scores = ['flux']
foil_tally_4.filters = [openmc.CellFilter(99)]
tallies.append(foil_tally_4)

# foil 5
foil_tally_5 = openmc.Tally(name='foil_5')
foil_tally_5.scores = ['flux']
foil_tally_5.filters = [openmc.CellFilter(116)]
tallies.append(foil_tally_5)

# foil 6
foil_tally_6 = openmc.Tally(name='foil_6')
foil_tally_6.scores = ['flux']
foil_tally_6.filters = [openmc.CellFilter(16)]
tallies.append(foil_tally_6)

# foil 7
foil_tally_7 = openmc.Tally(name='foil_7')
foil_tally_7.scores = ['flux']
foil_tally_7.filters = [openmc.CellFilter(59)]
tallies.append(foil_tally_7)

# foil 8
foil_tally_8 = openmc.Tally(name='foil_8')
foil_tally_8.scores = ['flux']
foil_tally_8.filters = [openmc.CellFilter(18)]
tallies.append(foil_tally_8)

# foil 9
foil_tally_9 = openmc.Tally(name='foil_9')
foil_tally_9.scores = ['flux']
foil_tally_9.filters = [openmc.CellFilter(70)]
tallies.append(foil_tally_9)

# foil 10
foil_tally_10 = openmc.Tally(name='foil_10')
foil_tally_10.scores = ['flux']
foil_tally_10.filters = [openmc.CellFilter(92)]
tallies.append(foil_tally_10)

# foil 11
foil_tally_11 = openmc.Tally(name='foil_11')
foil_tally_11.scores = ['flux']
foil_tally_11.filters = [openmc.CellFilter(51)]
tallies.append(foil_tally_11)

# foil 12
foil_tally_12 = openmc.Tally(name='foil_12')
foil_tally_12.scores = ['flux']
foil_tally_12.filters = [openmc.CellFilter(37)]
tallies.append(foil_tally_12)

# foil 13
foil_tally_13 = openmc.Tally(name='foil_13')
foil_tally_13.scores = ['flux']
foil_tally_13.filters = [openmc.CellFilter(79)]
tallies.append(foil_tally_13)

# foil 14
foil_tally_14 = openmc.Tally(name='foil_14')
foil_tally_14.scores = ['flux']
foil_tally_14.filters = [openmc.CellFilter(60)]
tallies.append(foil_tally_14)

# foil 15
foil_tally_15 = openmc.Tally(name='foil_15')
foil_tally_15.scores = ['flux']
foil_tally_15.filters = [openmc.CellFilter(107)]
tallies.append(foil_tally_15)

# foil 16
foil_tally_16 = openmc.Tally(name='foil_16')
foil_tally_16.scores = ['flux']
foil_tally_16.filters = [openmc.CellFilter(49)]
tallies.append(foil_tally_16)

# foil 17
foil_tally_17 = openmc.Tally(name='foil_17')
foil_tally_17.scores = ['flux']
foil_tally_17.filters = [openmc.CellFilter(90)]
tallies.append(foil_tally_17)

# foil 18
foil_tally_18 = openmc.Tally(name='foil_18')
foil_tally_18.scores = ['flux']
foil_tally_18.filters = [openmc.CellFilter(105)]
tallies.append(foil_tally_18)

# foil 19
foil_tally_19 = openmc.Tally(name='foil_19')
foil_tally_19.scores = ['flux']
foil_tally_19.filters = [openmc.CellFilter(38)]
tallies.append(foil_tally_19)

# foil 20
foil_tally_20 = openmc.Tally(name='foil_20')
foil_tally_20.scores = ['flux']
foil_tally_20.filters = [openmc.CellFilter(24)]
tallies.append(foil_tally_20)

# foil 21
foil_tally_21 = openmc.Tally(name='foil_21')
foil_tally_21.scores = ['flux']
foil_tally_21.filters = [openmc.CellFilter(97)]
tallies.append(foil_tally_21)

# foil 22
foil_tally_22 = openmc.Tally(name='foil_22')
foil_tally_22.scores = ['flux']
foil_tally_22.filters = [openmc.CellFilter(50)]
tallies.append(foil_tally_22)

# foil 23
foil_tally_23 = openmc.Tally(name='foil_23')
foil_tally_23.scores = ['flux']
foil_tally_23.filters = [openmc.CellFilter(56)]
tallies.append(foil_tally_23)

# foil 24
foil_tally_24 = openmc.Tally(name='foil_24')
foil_tally_24.scores = ['flux']
foil_tally_24.filters = [openmc.CellFilter(42)]
tallies.append(foil_tally_24)

# foil 25
foil_tally_25 = openmc.Tally(name='foil_25')
foil_tally_25.scores = ['flux']
foil_tally_25.filters = [openmc.CellFilter(28)]
tallies.append(foil_tally_25)

# foil 26
foil_tally_26 = openmc.Tally(name='foil_26')
foil_tally_26.scores = ['flux']
foil_tally_26.filters = [openmc.CellFilter(11)]
tallies.append(foil_tally_26)

# foil 27
foil_tally_27 = openmc.Tally(name='foil_27')
foil_tally_27.scores = ['flux']
foil_tally_27.filters = [openmc.CellFilter(121)]
tallies.append(foil_tally_27)

# foil 28
foil_tally_28 = openmc.Tally(name='foil_28')
foil_tally_28.scores = ['flux']
foil_tally_28.filters = [openmc.CellFilter(96)]
tallies.append(foil_tally_28)

# foil 29
foil_tally_29 = openmc.Tally(name='foil_29')
foil_tally_29.scores = ['flux']
foil_tally_29.filters = [openmc.CellFilter(102)]
tallies.append(foil_tally_29)

# foil 30
foil_tally_30 = openmc.Tally(name='foil_30')
foil_tally_30.scores = ['flux']
foil_tally_30.filters = [openmc.CellFilter(131)]
tallies.append(foil_tally_30)

# foil 31
foil_tally_31 = openmc.Tally(name='foil_31')
foil_tally_31.scores = ['flux']
foil_tally_31.filters = [openmc.CellFilter(127)]
tallies.append(foil_tally_31)

# foil 32
foil_tally_32 = openmc.Tally(name='foil_32')
foil_tally_32.scores = ['flux']
foil_tally_32.filters = [openmc.CellFilter(29)]
tallies.append(foil_tally_32)

tallies.export_to_xml()

model = openmc.model.Model(geom, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)

# extract flux mean for each tally and normalize to compare
