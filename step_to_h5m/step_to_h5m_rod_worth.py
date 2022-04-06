###############################################################################
# Converting step files to h5m file to be read by openmc

# Creates h5m file from step files for each rod position
# 0in. withdrawn - 36in. withdrawn (full) at one inch increments

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/material_tag
###############################################################################

from cad_to_h5m import cad_to_h5m
import numpy as np
import os

###############################################################################
#inputs
h5m_out_filepath = os.getcwd() + '/h5m_files/rod_worth/zpre'
local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

# positions from ORNL-2536 pg. 23
rod_pos = [0.00, 5.52, 6.18, 7.96, 8.075, 9.46, 10.66, 11.27, 12.384, 13.136,
           14.019, 14.705, 15.420, 16.00, 16.685, 16.809, 17.208, 17.775,
           18.285, 18.726, 19.201, 19.735, 20.489, 20.970, 21.284, 21.688,
           22.090, 22.475, 22.950, 23.350, 24.000, 24.155]
###############################################################################

#generating an h5m file for each rod position
for pos in rod_pos:
    cad_to_h5m(h5m_filename = h5m_out_filepath + '_pos_' + str(pos)[0:2]+ '.h5m',
            cubit_path=local_cubit_path,
            files_with_tags=[{"cad_filename": "../step_files/zpre_no_rod.step",
                             "transforms":{'scale':scale}},
                            {"cad_filename": "../step_files/zpre_rod_zero.step",
                             "transforms":{'scale':scale,'move':[0,0,-pos]}},
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
