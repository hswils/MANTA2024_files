import openmc

#TODO double check densities against reliable sources and stamp them as validated

# Pure elements/isotopes

hydrogen = openmc.Material(name='H1')
hydrogen.add_nuclide('H1',1.0)
hydrogen.set_density('atom/cm3',1e14) #1e20/m^3
deuterium = openmc.Material(name='H2')
deuterium.add_nuclide('H2',1.0)
deuterium.set_density('atom/cm3',1e14) #1e20/m^3
tritium = openmc.Material(name='H3')
tritium.add_nuclide('H3',1.0)
tritium.set_density('atom/cm3',1e14) #1e20/m^3

titanium = openmc.Material(name='Ti')
titanium.add_element('Ti',1.0)
titanium.set_density('g/cm3',4.5)

copper = openmc.Material(name='Cu')
copper.add_element('Cu',1.0)
copper.set_density('g/cm3',8.96)

silver = openmc.Material(name='Ag')
silver.add_element('Ag',1.0)
silver.set_density('g/cm3',10.49)

tungsten = openmc.Material(name='W')
tungsten.add_element('O',5/1e6,percent_type='wo')
tungsten.add_element('N',5/1e6,percent_type='wo')
tungsten.add_element('C',5/1e6,percent_type='wo')
tungsten.add_element('Na',4/1e6,percent_type='wo')
tungsten.add_element('K',2.5/1e6,percent_type='wo')
tungsten.add_element('Al',3/1e6,percent_type='wo')
tungsten.add_element('Ca',0.5/1e6,percent_type='wo')
tungsten.add_element('Cr',0.5/1e6,percent_type='wo')
tungsten.add_element('Cu',0.5/1e6,percent_type='wo')
tungsten.add_element('Fe',5/1e6,percent_type='wo')

tungsten.add_element('W',1-(5+5+5+4+2.5+3+0.5+0.5+0.5+5)/1e6,percent_type='wo')
tungsten.set_density('g/cm3',19.3)
tungsten.volume = 65636 #Wedge vol
tungsten.depletable = True


# Basic materials

flibe = openmc.Material(name='FLiBe')
flibe.add_elements_from_formula('F4Li2Be')
flibe.set_density('g/cm3',1.94)

y2o3 = openmc.Material(name='Y2O3')
y2o3.add_elements_from_formula('Y2O3')
y2o3.set_density('g/cm3',5.0)

pbsn = openmc.Material(name='PbSn Solder')
pbsn.add_element('Pb',0.37,percent_type='wo')
pbsn.add_element('Sn',0.63,percent_type='wo')
pbsn.set_density('g/cm3',8.8)

ybco = openmc.Material(name='YBCO')
ybco.add_elements_from_formula('YBa2Cu3O7')
ybco.set_density('g/cm3',6.3)

#3 Copies of the same material because the depletion library sucks...
vcrti_VV = openmc.Material(name='V-4Cr-4Ti VV')
vcrti_VV.volume = 221783 #Wedge vol
vcrti_VV.depletable = True
vcrti_BI = openmc.Material(name='V-4Cr-4Ti Blanket inner')
vcrti_BO = openmc.Material(name='V-4Cr-4Ti Blanket outer')
for m in [vcrti_VV,vcrti_BI,vcrti_BO]:
    #m.add_element('V',0.92,percent_type='wo')
    m.add_element('Cr',0.04,percent_type='wo')
    m.add_element('Ti',0.04,percent_type='wo')

    m.add_element('C',56/1e6,percent_type='wo')
    m.add_element('O',181/1e6,percent_type='wo')
    m.add_element('N',103/1e6,percent_type='wo')
    m.add_element('B',7/1e6,percent_type='wo')
    m.add_element('Na',17/1e6,percent_type='wo')
    m.add_element('Mg',0.5/1e6,percent_type='wo')
    m.add_element('Al',119/1e6,percent_type='wo')
    m.add_element('Si',280/1e6,percent_type='wo')
    m.add_element('Mn',0.5/1e6,percent_type='wo')
    m.add_element('Fe',80/1e6,percent_type='wo')
    m.add_element('Ni',13/1e6,percent_type='wo')
    m.add_element('Cu',4/1e6,percent_type='wo')
    m.add_element('V',1-0.04-0.04-(56+181+103+7+17+0.5+119+280+0.5+80+13+4)/1e6,percent_type='wo')
    m.set_density('g/cm3',6.05) #This density value is sus and needs a good source

sic = openmc.Material(name='SiC')
sic.add_element('C', 0.5, percent_type='ao')
sic.add_element('Si', 0.5, percent_type='ao')
sic.set_density('g/cm3', 3.21)

cucrzr = openmc.Material(name="CuCrZr")
cucrzr.add_element('Cu', 0.47, percent_type='wo')
cucrzr.add_element('Cr', 0.5, percent_type='wo')
cucrzr.add_element('Zr', 0.03, percent_type='wo')
cucrzr.set_density('g/cm3', 8.9)

fiberglass = openmc.Material(name='Fiberglass type E')
fiberglass.add_element('B', 0.022803, percent_type='wo')
fiberglass.add_element('O', 0.471950, percent_type='wo')
fiberglass.add_element('F', 0.004895, percent_type='wo')
fiberglass.add_element('Na', 0.007262, percent_type='wo')
fiberglass.add_element('Mg', 0.014759, percent_type='wo')
fiberglass.add_element('Al', 0.072536, percent_type='wo')
fiberglass.add_element('Si', 0.247102, percent_type='wo')
fiberglass.add_element('K', 0.008127, percent_type='wo')
fiberglass.add_element('Ca', 0.143428, percent_type='wo')
fiberglass.add_element('Ti', 0.004400, percent_type='wo')
fiberglass.add_element('Fe', 0.002739, percent_type='wo')
fiberglass.set_density('g/cm3', 2.57)

wc = openmc.Material(name='WC')
wc.add_element('W', 0.5, percent_type='ao')
wc.add_element('C', 0.5, percent_type='ao')
wc.set_density('g/cm3', 15.63)

wb = openmc.Material(name='WB')
wb.add_element('W', 0.5, percent_type='ao')
wb.add_element('B', 0.5, percent_type='ao')
wb.set_density('g/cm3', 12.91)

b4c = openmc.Material(name='B4C')
b4c.add_element('B', 0.8, percent_type='ao')
b4c.add_element('C', 0.2, percent_type='ao')
b4c.set_density('g/cm3', 2.52)

zd = openmc.Material(name='ZrD2')
zd.add_element('Zr', 1/3, percent_type='ao')
zd.add_nuclide('H2', 2/3, percent_type='ao')
zd.set_density('g/cm3', 5.56)


# Steels

hastelloy_c276 = openmc.Material(name='Hastelloy C276') #https://www.haynesintl.com/docs/default-source/pdfs/new-alloy-brochures/corrosion-resistant-alloys/brochures/c-276.pdf?sfvrsn=6
hastelloy_c276.add_element('Ni',0.5456,percent_type='wo')
hastelloy_c276.add_element('Co',0.025,percent_type='wo')
hastelloy_c276.add_element('Cr',0.16,percent_type='wo')
hastelloy_c276.add_element('Mo',0.16,percent_type='wo')
hastelloy_c276.add_element('Fe',0.05,percent_type='wo')
hastelloy_c276.add_element('W',0.04,percent_type='wo')
hastelloy_c276.add_element('Mn',0.01,percent_type='wo')
hastelloy_c276.add_element('V',0.0035,percent_type='wo')
hastelloy_c276.add_element('Si',0.0008,percent_type='wo')
hastelloy_c276.add_element('C',0.0001,percent_type='wo')
hastelloy_c276.add_element('Cu',0.005,percent_type='wo')
hastelloy_c276.set_density('g/cm3',8.89)

ss316ln = openmc.Material(name='SS 316LN')
ss316ln.add_element('Cr',0.18,percent_type='wo')
ss316ln.add_element('Ni',0.14,percent_type='wo')
ss316ln.add_element('Mo',0.025,percent_type='wo')
ss316ln.add_element('Mn',0.02,percent_type='wo')
ss316ln.add_element('Si',0.01,percent_type='wo')
ss316ln.add_element('N',0.003,percent_type='wo')
ss316ln.add_element('P',0.00045,percent_type='wo')
ss316ln.add_element('C',0.0003,percent_type='wo')
ss316ln.add_element('S',0.0003,percent_type='wo')
ss316ln.add_element('Fe',0.62095,percent_type='wo')
ss316ln.set_density('g/cm3',7.99)

eurofer = openmc.Material(name='Eurofer') #https://doi.org/10.1007/s10853-014-8281-5
eurofer.add_element('C',0.0011,percent_type='wo')
eurofer.add_element('Cr',0.087,percent_type='wo')
eurofer.add_element('W',0.01,percent_type='wo')
eurofer.add_element('Ta',0.001,percent_type='wo')
eurofer.add_element('V',0.0019,percent_type='wo')
eurofer.add_element('Mn',0.0044,percent_type='wo')
eurofer.add_element('S',0.00004,percent_type='wo')
eurofer.add_element('Fe',0.89456,percent_type='wo')
eurofer.set_density('g/cm3',7.80)

nitronic50 = openmc.Material(name='Nitronic 50') #https://www.premiumalloys.com/products/nitronic_50
nitronic50.add_element('Cr',0.22,percent_type='wo')
nitronic50.add_element('Ni',0.125,percent_type='wo')
nitronic50.add_element('Mo',0.0225,percent_type='wo')
nitronic50.add_element('Nb',0.002,percent_type='wo')
nitronic50.add_element('Mn',0.05,percent_type='wo')
nitronic50.add_element('Si',0.004,percent_type='wo')
nitronic50.add_element('C',0.0003,percent_type='wo')
nitronic50.add_element('S',0.0001,percent_type='wo')
nitronic50.add_element('P',0.0004,percent_type='wo')
nitronic50.add_element('V',0.0002,percent_type='wo')
nitronic50.add_element('N',0.003,percent_type='wo')
nitronic50.add_element('Fe',0.5725,percent_type='wo')
nitronic50.set_density('g/cm3',7.88)

# Complex mixes

tape = openmc.Material.mix_materials([copper,silver,hastelloy_c276,ybco],[10/65.35,3/65.35,50/65.35,2.35/65.35],percent_type='vo') #https://doi.org/10.1038/s41598-021-81559-z. Assuming 50um hastelloy.
windingpack = openmc.Material.mix_materials([copper,nitronic50,pbsn,tape],[0.163333,0.603333,0.030967,0.202367],percent_type='vo',name="Winding pack") #Volume fractions based on talks with magnet team

ods_batch_A = openmc.Material.mix_materials([eurofer,y2o3],[0.996,0.004],percent_type='wo') #Taken from https://doi.org/10.1016/j.msea.2021.141288
ods_batch_B = openmc.Material.mix_materials([eurofer,y2o3,titanium],[0.992,0.004,0.004],percent_type='wo') #Taken from https://doi.org/10.1016/j.msea.2021.141288
ods = openmc.Material.mix_materials([ods_batch_A,ods_batch_B],[1/3,2/3],percent_type='wo',name='ODS') #Taken from https://doi.org/10.1016/j.msea.2021.141288
ods.set_density('g/cm3',7.78)
