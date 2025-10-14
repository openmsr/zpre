import pyvista as pv
import vtk
import openmc
import numpy as np
import h5py

sp=openmc.StatePoint('fromU/statepoint.100.h5')
tl=sp.get_tally(name='flux3d')
sl=tl.get_slice(scores=['flux'])
sl.mean.shape=(300,300,300)
sl.std_dev.shape=sl.mean.shape



pl1=pv.Plotter(shape=(1,1),border=True)

# Create the spatial reference
grid = pv.UniformGrid()
grid.dimensions = sl.mean.shape

# Edit the spatial reference
grid.origin = (-125,-125,-25)  # The bottom left corner of the data set
grid.spacing = (2.5/6, 2.5/6, 2.5/6)  # These are the cell sizes along each axis

# Add the data values to the point data
grid.point_data["values"] = np.log(sl.mean.flatten(order="c")+1)  # Flatten the array!
slice1=grid.slice(normal=[1,0,1])
#use normalized values here - otherwise the plots may become completely obscured
vol=pv.wrap(sl.mean/np.mean(sl.mean))

pl1.theme.font.color='k'
pl1.set_background('w')
pl1.show_grid()
pl1.add_mesh(slice1, show_scalar_bar=False,cmap='GnBu')


#pl1.show(screenshot='output.png')


pl2=pv.Plotter()
hf=h5py.File('voxelplot.h5')
voxel_array=np.array(hf.get('data'))
geom= pv.UniformGrid()
geom.origin=(-300,-300,-300)
geom.dimensions=voxel_array.shape
geom.point_data["values"]=voxel_array.flatten(order='c')

pl2.add_mesh(geom)
pl2.show_grid()
