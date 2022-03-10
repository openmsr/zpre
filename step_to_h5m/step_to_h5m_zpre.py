###############################################################################
# Converting step files to h5m file to be read by openmc

# This script uses the following cad_to_h5m version
# https://github.com/openmsr/cad_to_h5m/tree/material_tag
###############################################################################
from cad_to_h5m import *
import numpy as np
import os
###############################################################################
# inputs

h5m_out_filepath = os.getcwd()  + '/h5m_files/ARE.h5m'
local_cubit_path = "/opt/Coreform-Cubit-2021.11/bin/"

# scaling up from cm and for thermal expansion
expansion_coefficient = 15.8e-6
operating_temperature = 954.2611
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

cad_to_h5m(h5m_filename= 'h5m_files/zpre.h5m',
            cubit_path="/opt/Coreform-Cubit-2021.11/bin/",
            files_with_tags=[{"cad_filename": "step_files/zpre.step",
                             "transforms":{'scale':scale}}
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
