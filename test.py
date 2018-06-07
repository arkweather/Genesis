import numpy as np 
import matplotlib.pyplot as plt
import pyart

RADAR_FILE = 'C:/Users/dave1/Desktop/Weather Report/GR2Analyst/Archived Data/Oklahoma 20150506/KTLX20150506_235157_V06.gz'
radar = pyart.io.read_nexrad_archive(RADAR_FILE)

# mask out last 10 gates of each ray, this removes the "ring" around th radar.
radar.fields['reflectivity']['data'][:, -10:] = np.ma.masked

# exclude masked gates from the gridding
gatefilter = pyart.filters.GateFilter(radar)
gatefilter.exclude_transition()
gatefilter.exclude_below('reflectivity', 10)
gatefilter.exclude_masked('reflectivity')

# perform Cartesian mapping, limit to the reflectivity field.
grid = pyart.map.grid_from_radars(
    (radar,), gatefilters=(gatefilter, ),
    grid_shape=(1, 241, 241),
    grid_limits=((2000, 2000), (-100000.0, 100000.0), (-100000.0, 100000.0)),
    fields=['reflectivity'])

print radar.gate_altitude['data'][0]

# create the plot
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.imshow(grid.fields['reflectivity']['data'][0], origin='lower', cmap = plt.get_cmap('gist_ncar'), vmin=-30, vmax=75)
# plt.show()
