import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
#create .png file of photon flux (boron sleeves fully inserted)
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
settings.photon_transport = True
source_area = openmc.stats.Box([-200., -200., -200.],[ 200.,  200.,  200.],only_fissionable = True)
settings.source = openmc.Source(space=source_area)
settings.export_to_xml()

#tallies
tallies = openmc.Tallies()

# sets up filters for the tallies
photon_particle_filter = openmc.ParticleFilter(['photon'])  # note the use of photons here
energy_bins = openmc.mgxs.GROUP_STRUCTURES['VITAMIN-J-175']
energy_filter = openmc.EnergyFilter(energy_bins)


mesh = openmc.RegularMesh()
mesh.dimension = [1000,1000]
mesh.lower_left = [-300,-300]
mesh.upper_right = [300,300]

mesh_filter = openmc.MeshFilter(mesh)

tally = openmc.Tally(name='flux')
tally.filters = [mesh_filter,photon_particle_filter]
tally.scores = ['flux']
tallies.append(tally)

tallies.export_to_xml()

# combine all the required parts to make a model
model = openmc.model.Model(geometry, mats, settings, tallies)

# remove old files and runs OpenMC
sp_filename = model.run()
sp = openmc.StatePoint(sp_filename)
s_tally = sp.get_tally(scores=['flux'])

flux = s_tally.get_slice(scores=['flux'])

flux.std_dev.shape = (1000,1000)
flux.mean.shape = (1000,1000)

fig,ax = plt.subplots()
ax.imshow(flux.mean,extent=[-300,300,-300,300])
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('photon flux')
plt.savefig('photon_flux')

fig,ax = plt.subplots()
ax.imshow(np.log(flux.mean),extent=[-300,300,-300,300])
ax.set_xlabel('X / cm')
ax.set_ylabel('Y / cm')
ax.set_title('photon flux[log]')
plt.savefig('photon_flux_log')
