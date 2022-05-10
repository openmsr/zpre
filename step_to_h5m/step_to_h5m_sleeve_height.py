###############################################################################
# Converting step files to h5m file to be read by openmc

# Creates h5m file from step files for boron sleeve position

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/move_volumes
###############################################################################

from cad_to_h5m import cad_to_h5m
import numpy as np
import os

###############################################################################

#inputs
h5m_out_filepath = os.getcwd() + '/h5m_files/sleeve_height/zpre'
local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

#scaling from up to cm & thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 977
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

# positions from ORNL-2536 pg. 37
sleeve_heights_inner = [0.5, 1.3, 3.0, 5.5, 6, 0.5, 6]
sleeve_heights_outer = [0.5, 1.3, 3.0, 5.5, 6, 6, 0.5]
###############################################################################

#generating an h5m file for each rod position
# inner boron sleeve: 27, 45, 67, 72
# outer boron sleeve: 7, 8, 15, 26
for i, pos in enumerate(sleeve_heights_inner):
    step_filename = os.getcwd() + '/step_files/zpre.step'
    cad_to_h5m(h5m_filename = h5m_out_filepath + '_sleeves_' + str(i) + '.h5m',
            cubit_path=local_cubit_path,
            files_with_tags=[{"cad_filename": step_filename,
                             "transforms":{'scale':scale,'move':([27,45,67,72,
                                                                  7,8,15,26],
                                                                  [[0,0,2.54*(5.937-pos)],
                                                                   [0,0,2.54*(5.937-pos)],
                                                                   [0,0,2.54*(5.937-pos)],
                                                                   [0,0,2.54*(5.937-pos)],
                                                                   [0,0,2.54*(5.937-sleeve_heights_outer[i])],
                                                                   [0,0,2.54*(5.937-sleeve_heights_outer[i])],
                                                                   [0,0,2.54*(5.937-sleeve_heights_outer[i])],
                                                                   [0,0,2.54*(5.937-sleeve_heights_outer[i])]])}}],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 500
                        )
