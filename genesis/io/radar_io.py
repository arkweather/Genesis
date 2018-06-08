from genesis.data.radar import Radar
import pyart
import numpy as np
import os

def correct_radar(radar):
	"""Performs all data correction such as dealiasing velocities, etc
	:param radar: A pyart radar file
	:return: The corrected pyart radar file
	"""
	
	

def load_single_file(directory, filename):
	"""Loads a single radar file and returns a Radar object
	
	:param directory: location of the file
	:param filename: name of the file including extension
	:return: Radar object (See genesis.data.radar)
	"""
	
	# Load the file
	if not directory.endswith('/'): directory += '/'
	
	RADAR_FILE = directory + filename
	radar = pyart.io.read(RADAR_FILE)
	
	# Perform all radar corrections
	
	
	
