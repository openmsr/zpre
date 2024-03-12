###############################################################################
# Converting step files to h5m file to be read by openmc
###############################################################################
import numpy as np
import os
import pathlib as pl
import CAD_to_OpenMC.assembly as ab
###############################################################################

# inputs
step_files=[pl.Path('step_files') / pl.Path(s) for s in ['zpre_core.step','zpre_control_rod.step','zpre_source.step','zpre_core_simplified.step']]
h5m_files=[pl.Path('h5m_files') / pl.Paths(h.parts[-1]).with_suffix('.h5m') for h in step_files] 

# mesher config
ab.mesher_config['threads'] = 1
ab.mesher_config['tolerance'] = 0.01

# output
for s,h in zip(step_files,h5m_files):
  print(s,h)
  continue
  a.ab.Assembly([s])
  a.verbose=2
  a.run(backend='stl2',merge=True,h5m_filename=h)
