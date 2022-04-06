import openmc
import numpy as np
from materials import *

###############################################################################
# rod worth simulation of zpre

# exports a .txt file with a k_eff at each position

# 0in. withdrawn - 24in. withdrawn (full) at one inch increments
###############################################################################

output_filename = 'k_effs.txt'

#equilibrium operating temperature in kelvin
operating_temp = 911.15

def build_model(dagmc_file):

    mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                             helium,scintillator,insulation,bepo,lindsay,gold,
                             aluminum,dt,fuel])
    mats.export_to_xml()

    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = 100
    settings.inactive = 10
    settings.particles = 10000
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(dagmc_file)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

shim_rod_positions = [0.00, 5.52, 6.18, 7.96, 8.075, 9.46, 10.66, 11.27, 12.384, 13.136,
           14.019, 14.705, 15.420, 16.00, 16.685, 16.809, 17.208, 17.775,
           18.285, 18.726, 19.201, 19.735, 20.489, 20.970, 21.284, 21.688,
           22.090, 22.475, 22.950, 23.350, 24.000, 24.155]
h5m_filenames = ['h5m_files/rod_worth/zpre_pos_' + str(i)[0:2] + '.h5m' for i in shim_rod_positions]
k_effs_simulated = []

#writing to text file
k_file = open(output_filename, 'w+')

for filename in h5m_filenames:
    model = build_model(filename)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        k_eff = sp.k_combined
        k_effs_simulated.append(k_eff.nominal_value)
        k_file.write("%s\n" %k_eff.nominal_value)

k_file.close()
