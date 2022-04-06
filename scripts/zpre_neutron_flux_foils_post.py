import matplotlib.pyplot as plt
import openmc
from materials import *

###############################################################################
# create comparison plots of neutron flux distribution
# normalized against 4th meaurement (see ORNL-2536 pg. 51)
###############################################################################

sp_filename = 'statepoint.200.h5'
sp = openmc.StatePoint(sp_filename)


# extract flux mean for each tally and normalize to compare

# experimental values
# ORNL-2536 pg. 51
distance_m = [0.190, 1.125, 2.125, 3.125, 3.875, 4.625, 5.375, 6.375, 7.375,
              8.875, 10.375, 13.010]
midplane_e = [0.473, 0.687, 0.866, 1.000, 0.998, 0.947, 0.855, 0.739, 0.595, 0.450,
            0.269, 0.063]

distance_e = [0.190, 1.125, 2.125, 3.125, 3.875, 4.625, 5.375, 6.375, 7.375,
              8.875, 10.375, 11.710]
eight_below_e = [0.478, 0.826, 0.998, 1.008, 0.951, 0.841, 0.847, 0.711, 0.610,
               0.420, 0.257, 0.095]

distance_s = [0.190, 1.125, 2.125, 2.875, 3.625, 4.375, 6.500, 7.935]
sixteen_below_e = [0.217, 0.414, 0.412, 0.600, 0.613, 0.559, 0.350, 0.122]

# tally values (normalized against 4th measurement)
# at midplane
f1 = sp.get_tally(name='foil_1')
f2 = sp.get_tally(name='foil_2')
f3 = sp.get_tally(name='foil_3')
f4 = sp.get_tally(name='foil_4')
f5 = sp.get_tally(name='foil_5')
f6 = sp.get_tally(name='foil_6')
f7 = sp.get_tally(name='foil_7')
f8 = sp.get_tally(name='foil_8')
f9 = sp.get_tally(name='foil_9')
f10 = sp.get_tally(name='foil_10')
f11 = sp.get_tally(name='foil_11')
f12 = sp.get_tally(name='foil_12')

midplane_s = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]
midplane_s_m = [f.get_pandas_dataframe().iloc[0]['mean'] for f in midplane_s]
midplane_s_e = [f.get_pandas_dataframe().iloc[0]['std. dev.'] for f in midplane_s]
norm = midplane_s_m[3]
midplane_s_m = [f/norm for f in midplane_s_m]
midplane_s_e = [f/norm for f in midplane_s_e]

# 8 in. below midplane
f13 = sp.get_tally(name='foil_13')
f14 = sp.get_tally(name='foil_14')
f15 = sp.get_tally(name='foil_15')
f16 = sp.get_tally(name='foil_16')
f17 = sp.get_tally(name='foil_17')
f18 = sp.get_tally(name='foil_18')
f19 = sp.get_tally(name='foil_19')
f20 = sp.get_tally(name='foil_20')
f21 = sp.get_tally(name='foil_21')
f22 = sp.get_tally(name='foil_22')
f23 = sp.get_tally(name='foil_23')
f24 = sp.get_tally(name='foil_24')


eight_below_s = [f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24]
eight_below_s_m = [f.get_pandas_dataframe().iloc[0]['mean'] for f in eight_below_s]
eight_below_s_e = [f.get_pandas_dataframe().iloc[0]['std. dev.'] for f in eight_below_s]
eight_below_s_m = [f/norm for f in eight_below_s_m]
eight_below_s_e = [f/norm for f in eight_below_s_e]

# 16 in. below midplane
f25 = sp.get_tally(name='foil_25')
f26 = sp.get_tally(name='foil_26')
f27 = sp.get_tally(name='foil_27')
f28 = sp.get_tally(name='foil_28')
f29 = sp.get_tally(name='foil_29')
f30 = sp.get_tally(name='foil_30')
f31 = sp.get_tally(name='foil_31')
f32 = sp.get_tally(name='foil_32')

sixteen_below_s = [f25, f26, f27, f28, f29, f30, f31, f32]
sixteen_below_s_m = [f.get_pandas_dataframe().iloc[0]['mean'] for f in sixteen_below_s]
sixteen_below_s_e = [f.get_pandas_dataframe().iloc[0]['std. dev.'] for f in sixteen_below_s]
sixteen_below_s_m = [f/norm for f in sixteen_below_s_m]
sixteen_below_s_e = [f/norm for f in sixteen_below_s_e]

# generate plots
# midplane
fig_m, ax_m = plt.subplots()
ax_m.plot(distance_m,midplane_e,label = 'experimental',linestyle='--',marker='x')
ax_m.errorbar(distance_m,midplane_s_m, yerr=midplane_s_e,label = 'simulated',linestyle='--',marker='o')
ax_m.set_xlabel('distance (in.)')
ax_m.set_ylabel('relative neutron flux')
ax_m.set_title('neutron flux distribution - midplane')
ax_m.legend()

# 8 in. below
fig_8, ax_8 = plt.subplots()
ax_8.plot(distance_e,eight_below_e,label = 'experimental',linestyle='--',marker='x')
ax_8.errorbar(distance_e,eight_below_s_m,yerr=eight_below_s_e,label = 'simulated',linestyle='--',marker='o')
ax_8.set_xlabel('distance (in.)')
ax_8.set_ylabel('relative neutron flux')
ax_8.set_title('neutron flux distribution - 8 in. below midplane')
ax_8.legend()

# 16 in. below
fig_16, ax_16 = plt.subplots()
ax_16.plot(distance_s,sixteen_below_e, label = 'experimental',linestyle='--',marker='x')
ax_16.errorbar(distance_s,sixteen_below_s_m,yerr=sixteen_below_s_e,label = 'simulated',linestyle='--',marker='o')
ax_16.set_xlabel('distance (in.)')
ax_16.set_ylabel('relative neutron flux')
ax_16.set_title('neutron flux distribution - 16 in. below midplane')
ax_16.legend()

plt.show()
