from itertools import count
import openmc
import numpy as np
from materials import *
import os
import matplotlib.pyplot as plt

###############################################################################
# rod worth simulation of zpre

# exports a .txt file with a k_eff at each position

# 0in. withdrawn - 24in. withdrawn (full) at one inch increments
###############################################################################

output_filename = 'k_effs.txt'

# equilibrium operating temperature in kelvin
operating_temp = 911.15

# create materials object
mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                             helium,scintillator,insulation,bepo,lindsay,gold,
                             aluminum,dt,fuel, boron])

def build_model(dagmc_file):

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

    # setting up tally at detector
    tallies = openmc.Tallies()
    scintillator = openmc.Tally(name='scintillator')
    scintillator.scores = ['flux']
    scintillator.filters = [openmc.CellFilter(58)]
    tallies.append(scintillator)
    tallies.export_to_xml()


    dag_univ = openmc.DAGMCUniverse(dagmc_file)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings,tallies)
    return model

h5m_filenames = os.listdir(os.getcwd()+'/h5m_files/sleeve_height/')
h5m_filenames.sort(key=lambda x:x[13])

# relative counting rates to initial position 
counting_rates_sim = []
err_sim = []

# ORNL-2536 pg 37
counting_rates_ex = [1.00, 0.94, 0.82, 0.63, 0.62, 0.70, 0.92]

# extracting tally 
k_file = open(output_filename, 'w+')

for filename in h5m_filenames:
    model = build_model(os.getcwd()+'/h5m_files/sleeve_height/'+filename)
    sp_filepath = model.run(output = True)

    with openmc.StatePoint(sp_filepath) as sp:
        if not counting_rates_sim:
            counting_rate.append(1.0)
            err_sim.append(0.0)
        else:
            counting_rate = sp.get_tally(name='foil_13')
            df = counting_rate.get_pandas_dataframe()
            mean_cr = df.iloc[0]['mean']
            std_cr = df.iloc[0]['std. dev.']
            counting_rate.append(mean_cr/counting_rates_sim[0])
            err_sim.append(std_cr/err_sim[0])

# plotting
x_vals = list(range(len(counting_rates_ex)))
fig, ax = plt.subplots()
ax.plot(x_vals,counting_rates_ex, label = 'experimental',linestyle='--',marker='x')
ax.errorbar(x_vals,counting_rates_sim,yerr=err_sim,label = 'simulated',linestyle='--',marker='o')
ax.set_xlabel('sleeve configuration (ORNL-2536 pg 37)')
ax.set_ylabel('relative neutron flux (counting rate)')
ax.set_title('relative neutron counting rates at detector')
ax.legend()

plt.show()
