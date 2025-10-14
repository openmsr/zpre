import matplotlib.pyplot as plt
import openmc
from materials import *
import numpy as np

###############################################################################
#create .png file of neutron flux (boron sleeves fully inserted)
###############################################################################

#Geometry
h5m_filepath = 'h5m_files/zpre.h5m'
graveyard = openmc.Sphere(r=10000,boundary_type='vacuum')
cad_univ = openmc.DAGMCUniverse(filename=h5m_filepath,auto_geom_ids=True)
cad_cell = openmc.Cell(region=-graveyard,fill=cad_univ)
root=openmc.Universe()
root.add_cells([cad_cell])
geometry=openmc.Geometry(root)
geometry.export_to_xml()

#materials
mats = openmc.Materials([inconel,reflector,b4c,hastelloyx,stainless,brass,
                         helium,scintillator,insulation,bepo,lindsay,gold,
                         aluminum,dt,fuel,boron])
mats.export_to_xml()

settings = openmc.Settings()
settings.temperature = {'method':'interpolation'}
settings.batches = 100
settings.inactive = 10
settings.particles = 5000
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#tallies
tallies = openmc.Tallies()

mesh = openmc.RegularMesh()
mesh.dimension = [100,100,100]
mesh.lower_left = [-100,-100,-100]
mesh.upper_right = [100,100,100]

mesh_filter = openmc.MeshFilter(mesh)

tally = openmc.Tally(name='flux')
tally.filters = [mesh_filter]
tally.scores = ['flux','fission']
tallies.append(tally)

tallies.export_to_xml()

model = openmc.model.Model(geometry, mats, settings, tallies)
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)

s_tally = sp.get_tally(scores=['flux','fission'])
flux = s_tally.get_slice(scores=['flux'])
fission = s_tally.get_slice(scores=['fission'])

flux.std_dev.shape = (100,100,100)
flux.mean.shape = (100,100,100)
fission.std_dev.shape = (100,100,100)
fission.mean.shape = (100,100,100)


split_index = int(100/2)
# xy plot
xy_mean = flux.mean[split_index,:,:]
fig,ax = plt.subplots()
ax.imshow(xy_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('mean neutron flux: xy plane')
plt.savefig('neutron_flux_xy')

# xz plot
xz_mean = flux.mean[:,split_index, :]
fig,ax = plt.subplots()
ax.imshow(xz_mean)
ax.set_xlabel('X / cm')
ax.set_ylabel('Z / cm')
ax.set_title('mean neutron flux: xz plane')
plt.savefig('neutron_flux_xz')

# yz plot
yz_mean = flux.mean[:,:,split_index]
fig,ax = plt.subplots()
ax.imshow(yz_mean)
ax.set_xlabel('Y / cm')
ax.set_ylabel('Z / cm')
ax.set_title('mean neutron flux: yz plane')
plt.savefig('neutron_flux_yz')

#fig,ax = plt.subplots()
#ax.imshow(flux.mean,extent=[mesh.lower_left[0], mesh.upper_right[0],mesh.lower_left[1],mesh.upper_right[1]])
#ax.set_xlabel('X / cm')
#ax.set_ylabel('Y / cm')
#ax.set_title('neutron flux')
#plt.savefig('neutron_flux')

#fig,ax = plt.subplots()
#ax.imshow(np.log(flux.mean+1),extent=[mesh.lower_left[0], mesh.upper_right[0],mesh.lower_left[1],mesh.upper_right[1]])
#ax.set_xlabel('X / cm')
#ax.set_ylabel('Y / cm')
#ax.set_title('neutron flux[log]')
#plt.savefig('neutron_flux_log')

#fig,ax = plt.subplots()
#ax.imshow(fission.mean,extent=[mesh.lower_left[0], mesh.upper_right[0],mesh.lower_left[1],mesh.upper_right[1]])
#ax.set_xlabel('X / cm')
#ax.set_ylabel('Y / cm')
#ax.set_title('fission events')
#plt.savefig('fission_evts')

#fig,ax = plt.subplots()
#ax.imshow(np.log(fission.mean+1),extent=[mesh.lower_left[0], mesh.upper_right[0],mesh.lower_left[1],mesh.upper_right[1]])
#ax.set_xlabel('X / cm')
#ax.set_ylabel('Y / cm')
#ax.set_title('fission events [log]')
#plt.savefig('fission_evts_log')
