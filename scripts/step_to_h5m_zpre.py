###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_filepath = "./step_files/zpre_simplified.step"
step_filepath = "zpre_noint.step"
#step_filepath = "test_blocks.step"
#step_filepath = "loop6.1_b26.6.step"
h5m_out_filepath = os.getcwd() + '/h5m_files/zpre_noint2.h5m'

# mesher config
#ab.mesher_config['min_mesh_size'] =  
ab.mesher_config['mesh_algorithm'] = 2
ab.mesher_config['threads'] = 1
ab.mesher_config['curve_samples'] = 50
#ab.mesher_config['refine']=0
#ab.mesher_config['max_mesh_size'] = 1000
#ab.mesher_config['vetoed'] = [474,1157,1243,1341,1537]
ab.mesher_config['angular_tolerance'] = 0.10

ab.mesher_config['tolerance'] = 0.2

# output
a=ab.Assembly()
a.verbose=2
a.stp_files=[step_filepath]
a.import_stp_files()
a.merge_all()
a.solids_to_h5m(backend='stl2',h5m_filename=h5m_out_filepath)
