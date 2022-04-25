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
h5m_out_filepath = os.getcwd() + '/h5m_files/fuel_height/zpre'
local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

# positions from ORNL-2536 pg. 23
fuel_heights = [0, 1, 3, 5, 7]

###############################################################################

#generating an h5m file for each rod position
for pos in fuel_heights:
    step_filename = os.getcwd() + '/step_files/fuel_height/' + 'zpre_fuel_' + str(pos) + '.step'
    cad_to_h5m(h5m_filename = h5m_out_filepath + '_fuel_' + str(pos) + '.h5m',
            cubit_path=local_cubit_path,
            files_with_tags=[{"cad_filename": step_filename,
                             "transforms":{'scale':scale}}
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 500
                        )
