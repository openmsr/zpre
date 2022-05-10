import openmc
import numpy as np
from materials import *
from cad_to_h5m import cad_to_h5m
import os
import matplotlib.pyplot as plt

###############################################################################
# rod worth simulation of zpre

# plots rod position at criticality
###############################################################################

#equilibrium operating temperature in kelvin
operating_temp = 911.15

def find_pos(h5m_file,k_rel):
    """
    Returns how far, in inches, rod needs to be moved to reach criticality 
    """
    # fuel height
    height = h5m_file.split('.')[0][-1]

    # reference at 3.25 in. above midplane (fuel touching fuel probe)
    k_new = 0
    adj = 0
    while k_new < k_rel:
        k_new  = move_rod(adj,1,height)
        adj -= 1./2.54
    
    return adj

def move_rod(pos,distance,start):

    h5m_out_filepath = os.getcwd()  + '/h5m_files/fuel_height/zpre'
    local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

    # scaling up from cm and for thermal expansion
    expansion_coefficient = 15.8e-6
    scale = 100.*(1.0 + expansion_coefficient*(operating_temp-293))

    # move rod 
    # 1, 2, 46, 80, 100 are the volume ids of the control rod assembly (identified via cubit gui)
    cad_to_h5m(h5m_filename = h5m_out_filepath + '_pos_'+str(pos-1./2.54)[0:2]+'.h5m',
            cubit_path=local_cubit_path,
            files_with_tags=[{"cad_filename": "./step_files/fuel_height/zpre_fuel_"+str(start)+'.step',
                             "transforms":{'scale':scale,'move':([1,2,46,80,100],[0,0,-pos*2.54-distance])}},
                            {"cad_filename": "./step_files/zpre_control_rod_zero.step",
                             "transforms":{'scale':scale,'move':[0,0,-pos*2.54-distance]}},
                            ],
            faceting_tolerance = 1e-3,
            implicit_complement_material_tag = "helium",
            graveyard = 500
            )

    # find k 
    model_new = build_model(h5m_out_filepath)
    sp_new = model_new.run(output=True)
    k_upd = sp_new.k_combined
    return k_upd



def build_model(dagmc_file):

    mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                             helium,scintillator,insulation,bepo,lindsay,gold,
                             aluminum,dt,fuel,boron])
    mats.export_to_xml()

    settings = openmc.Settings()
    settings.temperature = {'method':'interpolation'}
    settings.batches = 100
    settings.inactive = 10
    settings.particles = 10000
    settings.export_to_xml()
    source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.])
    settings.source = openmc.Source(space=source_area)
    settings.export_to_xml()

    dag_univ = openmc.DAGMCUniverse(dagmc_file)
    geom = openmc.Geometry(root=dag_univ)
    geom.export_to_xml()

    model = openmc.model.Model(geom,mats,settings)
    return model

# fuel height values represent inches below fill probe
fuel_heights = [0, 1, 3, 5, 7]

# find position for criticality (relative to zero height)
h5m_filenames = os.listdir(os.getcwd()+'/h5m_files/fuel_height')

# get k for zero pos
zero_model = build_model('./h5m_files/fuel_height/zpre_fuel_0.h5m')
sp = zero_model.run(output=True)
k_zero = sp.k_combined

# find positions 
crit_pos = [19.74]
for f in h5m_filenames[1:]:
    crit_pos.append(crit_pos[-1]-find_pos(f,k_zero))

# plotting 
crit_pos_ex = [19.74, 19.53, 18.61, 16.93, 13.36]
plt.plot(fuel_heights,crit_pos,linestyle='--',marker='.',label='simulated')
plt.plot(fuel_heights,crit_pos,linestyle='--',marker='.',label='experimental')
plt.xlabel('fuel height (in.)')
plt.ylabel('rod position (in. inserted)')
plt.legend()
plt.show()
