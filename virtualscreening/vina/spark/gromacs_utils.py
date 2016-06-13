import os

""" This function gets value from xvg file
that was generated by gmx sasa
"""
def get_value_from_xvg_sasa(path_file):
	area_value = -1
	f_xvg = open(path_file)
	for line in f_xvg:
		area_value = float(str(line).split()[2])
	f_xvg.close()
	return area_value

