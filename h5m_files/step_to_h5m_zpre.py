###############################################################################
# Convert all zpre parts to an h5m file
###############################################################################


from cad_to_h5m import cad_to_h5m
import numpy as np

expansion_coefficient = 15.8e-6
operating_temperature = 954.2611
scale = 100.*(1.0 + expansion_coefficient*(operating_temperature-293))

cad_to_h5m(h5m_filename= 'zpre_1.h5m',
            cubit_path="/opt/Coreform-Cubit-2021.5/bin/",
            files_with_tags=[{"cad_filename": "step_files/zpre.step"}
                            ],
                        faceting_tolerance = 1e-3,
                        implicit_complement_material_tag = "helium",
                        graveyard = 1000
                        )
