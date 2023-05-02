import matplotlib.pyplot as plt
import openmc
from materials import *

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
settings.particles = 1000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

# tallies
tallies = openmc.Tallies()

# cell ids determined from volume ids in output of meshing step
# at midplane
# foil 1
foil_tally_1 = openmc.Tally(name='foil_1')
foil_tally_1.scores = ['flux']
foil_tally_1.filters = [openmc.CellFilter(14),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_1)

# foil 2
foil_tally_2 = openmc.Tally(name='foil_2')
foil_tally_2.scores = ['flux']
foil_tally_2.filters = [openmc.CellFilter(31),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_2)

# foil 3
foil_tally_3 = openmc.Tally(name='foil_3')
foil_tally_3.scores = ['flux']
foil_tally_3.filters = [openmc.CellFilter(22),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_3)

# foil 4
foil_tally_4 = openmc.Tally(name='foil_4')
foil_tally_4.scores = ['flux']
foil_tally_4.filters = [openmc.CellFilter(25),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_4)

# foil 5
foil_tally_5 = openmc.Tally(name='foil_5')
foil_tally_5.scores = ['flux']
foil_tally_5.filters = [openmc.CellFilter(29),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_5)

# foil 6
foil_tally_6 = openmc.Tally(name='foil_6')
foil_tally_6.scores = ['flux']
foil_tally_6.filters = [openmc.CellFilter(2),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_6)

# foil 7
foil_tally_7 = openmc.Tally(name='foil_7')
foil_tally_7.scores = ['flux']
foil_tally_7.filters = [openmc.CellFilter(15),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_7)

# foil 8
foil_tally_8 = openmc.Tally(name='foil_8')
foil_tally_8.scores = ['flux']
foil_tally_8.filters = [openmc.CellFilter(3),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_8)

# foil 9
foil_tally_9 = openmc.Tally(name='foil_9')
foil_tally_9.scores = ['flux']
foil_tally_9.filters = [openmc.CellFilter(17),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_9)

# foil 10
foil_tally_10 = openmc.Tally(name='foil_10')
foil_tally_10.scores = ['flux']
foil_tally_10.filters = [openmc.CellFilter(21),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_10)

# foil 11
foil_tally_11 = openmc.Tally(name='foil_11')
foil_tally_11.scores = ['flux']
foil_tally_11.filters = [openmc.CellFilter(12),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_11)

# foil 12
foil_tally_12 = openmc.Tally(name='foil_12')
foil_tally_12.scores = ['flux']
foil_tally_12.filters = [openmc.CellFilter(7),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_12)


# 8 in. below midplane
# foil 13
foil_tally_13 = openmc.Tally(name='foil_13')
foil_tally_13.scores = ['flux']
foil_tally_13.filters = [openmc.CellFilter(19),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_13)

# foil 14
foil_tally_14 = openmc.Tally(name='foil_14')
foil_tally_14.scores = ['flux']
foil_tally_14.filters = [openmc.CellFilter(16),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_14)

# foil 15
foil_tally_15 = openmc.Tally(name='foil_15')
foil_tally_15.scores = ['flux']
foil_tally_15.filters = [openmc.CellFilter(28),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_15)

# foil 16
foil_tally_16 = openmc.Tally(name='foil_16')
foil_tally_16.scores = ['flux']
foil_tally_16.filters = [openmc.CellFilter(10),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_16)

# foil 17
foil_tally_17 = openmc.Tally(name='foil_17')
foil_tally_17.scores = ['flux']
foil_tally_17.filters = [openmc.CellFilter(20),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_17)

# foil 18
foil_tally_18 = openmc.Tally(name='foil_18')
foil_tally_18.scores = ['flux']
foil_tally_18.filters = [openmc.CellFilter(27),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_18)

# foil 19
foil_tally_19 = openmc.Tally(name='foil_19')
foil_tally_19.scores = ['flux']
foil_tally_19.filters = [openmc.CellFilter(8),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_19)

# foil 20
foil_tally_20 = openmc.Tally(name='foil_20')
foil_tally_20.scores = ['flux']
foil_tally_20.filters = [openmc.CellFilter(4),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_20)

# foil 21
foil_tally_21 = openmc.Tally(name='foil_21')
foil_tally_21.scores = ['flux']
foil_tally_21.filters = [openmc.CellFilter(24),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_21)

# foil 22
foil_tally_22 = openmc.Tally(name='foil_22')
foil_tally_22.scores = ['flux']
foil_tally_22.filters = [openmc.CellFilter(11),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_22)

# foil 23
foil_tally_23 = openmc.Tally(name='foil_23')
foil_tally_23.scores = ['flux']
foil_tally_23.filters = [openmc.CellFilter(13),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_23)

# foil 24
foil_tally_24 = openmc.Tally(name='foil_24')
foil_tally_24.scores = ['flux']
foil_tally_24.filters = [openmc.CellFilter(9),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_24)

# 16 in. below midplane
# foil 25
foil_tally_25 = openmc.Tally(name='foil_25')
foil_tally_25.scores = ['flux']
foil_tally_25.filters = [openmc.CellFilter(5),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_25)

# foil 26
foil_tally_26 = openmc.Tally(name='foil_26')
foil_tally_26.scores = ['flux']
foil_tally_26.filters = [openmc.CellFilter(1),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_26)

# foil 27
foil_tally_27 = openmc.Tally(name='foil_27')
foil_tally_27.scores = ['flux']
foil_tally_27.filters = [openmc.CellFilter(30),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_27)

# foil 28
foil_tally_28 = openmc.Tally(name='foil_28')
foil_tally_28.scores = ['flux']
foil_tally_28.filters = [openmc.CellFilter(23),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_28)

# foil 29
foil_tally_29 = openmc.Tally(name='foil_29')
foil_tally_29.scores = ['flux']
foil_tally_29.filters = [openmc.CellFilter(26),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_29)

# foil 30
foil_tally_30 = openmc.Tally(name='foil_30')
foil_tally_30.scores = ['flux']
foil_tally_30.filters = [openmc.CellFilter(3),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_30)

# foil 31
foil_tally_31 = openmc.Tally(name='foil_31')
foil_tally_31.scores = ['flux']
foil_tally_31.filters = [openmc.CellFilter(32),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_31)

# foil 32
foil_tally_32 = openmc.Tally(name='foil_32')
foil_tally_32.scores = ['flux']
foil_tally_32.filters = [openmc.CellFilter(6),openmc.EnergyFilter([0.0,10.0])]
tallies.append(foil_tally_32)

tallies.export_to_xml()

model = openmc.model.Model(geometry, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)
