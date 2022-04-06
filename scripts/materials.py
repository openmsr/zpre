import openmc


# equilibrium operating temperature in kelvin
operating_temp = 911.15

# thermal expansion coefficients
inconel_te = 15.8e-6
beo_te = 8e-6
hastelloyx_te = 15.9e-6
b4c_te = 4.5e-6
stainless_te = 9.9e-6
salt_te = 0.00093

# zpre material definitions

# inconel
trace = 0.01
inconel = openmc.Material(name='inconel',temperature = operating_temp)
inconel.add_element('Ni',78.5,percent_type='wo')
inconel.add_element('Cr',14.0,percent_type='wo')
inconel.add_element('Fe',6.5,percent_type='wo')
inconel.add_element('Mn',0.25,percent_type='wo')
inconel.add_element('Si',0.25,percent_type='wo')
inconel.add_element('Cu',0.2,percent_type='wo')
inconel.add_element('Co',0.2,percent_type='wo')
inconel.add_element('Al',0.2,percent_type='wo')
inconel.add_element('Ti',0.2,percent_type='wo')
inconel.add_element('Ta',0.5,percent_type='wo')
inconel.add_element('W',0.5,percent_type='wo')
inconel.add_element('Zn',0.2,percent_type='wo')
inconel.add_element('Zr',0.1,percent_type='wo')
inconel.add_element('C',trace,percent_type='wo')
inconel.add_element('Mo',trace,percent_type='wo')
inconel.add_element('Ag',trace,percent_type='wo')
inconel.add_element('B',trace,percent_type='wo')
inconel.add_element('Ba',trace,percent_type='wo')
inconel.add_element('Be',trace,percent_type='wo')
inconel.add_element('Ca',trace,percent_type='wo')
inconel.add_element('Cd',trace,percent_type='wo')
inconel.add_element('V',trace,percent_type='wo')
inconel.add_element('Sn',trace,percent_type='wo')
inconel.add_element('Mg',trace,percent_type='wo')
inconel.set_density('g/cm3',8.51-inconel_te*(operating_temp-293.15))

# beryllium reflectors
# ORNL-2536 pg. 92
reflector = openmc.Material(name='reflector',temperature = operating_temp)
reflector.add_element('Be',.98802182,percent_type='wo')
reflector.add_element('O',.009996092,percent_type='wo')
reflector.add_element('Fe',0.001370720,percent_type='wo')
reflector.add_element('Al',0.000281732,percent_type='wo')
reflector.add_element('Mn',0.000109262,percent_type='wo')
reflector.add_element('Li',0.000000300,percent_type='wo')
reflector.add_element('Co',0.000005223,percent_type='wo')
reflector.add_element('Ni',0.000213616,percent_type='wo')
reflector.add_element('Cd',0.000000200,percent_type='wo')
reflector.add_element('B',0.000001039,percent_type='wo')
reflector.set_density('g/cm3',2.55-beo_te*(operating_temp-293.15))

# boron in lower part of the reactor; boron carbide
b4c = openmc.Material(name = 'b4c', temperature = operating_temp)
b4c.add_element('B',4.0)
b4c.add_element('C',1.0)
b4c.set_density('g/cm3',2.52-b4c_te*(operating_temp-293.15))

# beryllium reflectors
# ORNL-2536 pg. 93
hastelloyx = openmc.Material(name = 'hastelloyx',temperature = operating_temp)
hastelloyx.add_element('Mo',0.080555143088425,percent_type='wo')
hastelloyx.add_element('Fe',0.179973488835191,percent_type='wo')
hastelloyx.add_element('Cr',0.226256918302626,percent_type='wo')
hastelloyx.add_element('Co',0.010178976879095,percent_type='wo')
hastelloyx.add_element('Mn',0.002306601900095,percent_type='wo')
hastelloyx.add_element('Ni',0.504147672628661,percent_type='wo')
hastelloyx.set_density('g/cm3',8.22-hastelloyx_te*(operating_temp-293.15))

# stainless https://www.aesteiron.com/sa240-304l-stainless-steel-sheet-plate.html
stainless = openmc.Material(name='stainless',temperature = operating_temp)
stainless.add_element('C',0.030,percent_type='wo')
stainless.add_element('Mn',2.00,percent_type='wo')
stainless.add_element('P',0.045,percent_type='wo')
stainless.add_element('S',0.030,percent_type='wo')
stainless.add_element('Si',0.75,percent_type='wo')
stainless.add_element('Cr',18.00,percent_type='wo')
stainless.add_element('Ni',8.0,percent_type='wo')
stainless.add_element('N',0.1,percent_type='wo')
stainless.set_density('g/cm3',8.5-stainless_te*(operating_temp-293.15))

# brass for scintillator can
brass = openmc.Material(name='brass',temperature = operating_temp)
brass.add_element('Cu',0.95,percent_type='wo')
brass.add_element('Zn',0.05,percent_type='wo')

#helium
helium = openmc.Material(name='helium',temperature = operating_temp)
helium.add_element('He',1.0)
helium.set_density('g/cm3',1.03*(10**-4))

# scintillator (zinc sulfide)
scintillator = openmc.Material(name='scintillator',temperature = operating_temp)
scintillator.add_element('Zn',1.0)
scintillator.add_element('S',1.0)
scintillator.set_density('g/cm3',4.09)

# insulation (calcinated diatamaceous silica)
insulation = openmc.Material(name='insulation', temperature = operating_temp)
insulation.add_element('Si',.2618,percent_type='wo')
insulation.add_element('Fe',.1846,percent_type='wo')
insulation.add_element('Zr',.0533,percent_type='wo')
insulation.add_element('Al',.0344,percent_type='wo')
insulation.add_element('Ti',.0090,percent_type='wo')
insulation.add_element('Sb',.0109,percent_type='wo')
insulation.add_element('Mn',.0018,percent_type='wo')
insulation.add_element('Zn',.0022,percent_type='wo')
insulation.add_element('Sn',.0016,percent_type='wo')
insulation.add_element('Ni',.0009,percent_type='wo')
insulation.add_element('Cu',.0444,percent_type='wo')
insulation.add_element('Pb',.0173,percent_type='wo')
insulation.add_element('O',.3778,percent_type='wo')
insulation.set_density('g/cm3',0.767)

# neutron source
bepo = openmc.Material(name='bepo', temperature = operating_temp)
bepo.add_element('Be',1.0)
bepo.add_element('Po',1.0)
bepo.set_density('g/cm3',7.30)

# lindsay mix cement
# ORNL-2536 pg. 83
# spreading "Misc." material evenly by weight
lindsay = openmc.Material(name='lindsay', temperature = operating_temp)
lindsay.add_element('N',0.70+0.70*0.042,percent_type='wo')
lindsay.add_element('Sm',0.30*0.638+0.30*0.638*0.042,percent_type='wo')
lindsay.add_element('Cd',0.30*0.263+0.30*0.263*0.042,percent_type='wo')
lindsay.add_element('Dy',0.30*0.048+0.30*0.048*0.042,percent_type='wo')
lindsay.add_element('Nd',0.30*0.009+0.30*0.009*0.042,percent_type='wo')
lindsay.set_density('g/cm3',2.3999999999999995)

# gold (gold foils)
gold = openmc.Material(name='gold', temperature = operating_temp)
gold.add_element('Au',1.0)
gold.set_density('g/cm3',19.3)

# aluminum oxide (in detector tubes)
aluminum = openmc.Material(name='aluminum', temperature = operating_temp)
aluminum.add_element('Al',2.0)
aluminum.add_element('O',3.0)
aluminum.set_density('g/cm3',3.95)

# detector tube
# consists of calcium flouride with uranium foils
# instead, defining as one material with average composition
dt = openmc.Material(name='dt', temperature = operating_temp)
dt.add_element('U',0.1258,percent_type='wo')
dt.add_elements_from_formula('CaF2',percent_type='wo')
dt.set_density('g/cm3',3.55)

#fuel fuel NaF-ZrF4-UF4 0.20082-0.65416-0.122 %mol
#ORNL-2536 pg. 3
fuel = openmc.Material(name='fuel', temperature = operating_temp)
fuel.add_element('F',0.2390,percent_type='wo')
fuel.add_element('Na',0.11,percent_type='wo')
fuel.add_element('Zr',0.5414,percent_type='wo')
fuel.add_nuclide('U235',0.0922,percent_type='wo')
fuel.add_nuclide('U238',0.0174,percent_type='wo')
fuel.set_density('g/cm3',4.16-salt_te*(operating_temp-273.15))

# enriched boron in boron sleeves
boron = openmc.Material(name='boron', temperature = operating_temp)
boron.add_nuclide('B10',0.92,percent_type='wo')
boron.add_element('O',0.0577,percent_type='wo')
boron.add_element('Fe',0.0023,percent_type='wo')
boron.set_density('g/cm3',1.5-b4c_te*(operating_temp-293.15))
