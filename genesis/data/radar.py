import pyart
import numpy as np

class Radar:

	def __init__(self, site = '', time = None, tilts = [], data = {}, lat = 0, lon = 0, rrange = 0):
		"""Constructor for the Radar class (seperate from the pyart Radar class)
		
		:param site: Name of the radar site
		:param time: Datetime of the volume product
		:param tilts: List of tilts scanned in the volume, in the order in which they occurred
		:param data: Dictionary containing the gridded radar data.  Should be structured as
					 {['Field']:[[data at each subsequent tilt]]}
		:param lat: Latitude of the radar
		:param lon: Longitude of the radar
		:param rrange: Maximum grid distance from the radar to display
		"""
		
		# Initial class variables
		self.time = time
		self.tilts = tilts
		self.data = data
		self.lat = lat
		self.lon = lon
		self.rrange = rrange
		
		
		
		
