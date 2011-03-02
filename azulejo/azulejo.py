#!/usr/bin/env python
#
# This script binds keyboard shortcuts to window resizing/tilling actions.
# To fine tune your settings, edit the file ~/.azulejorc.js
#
# Author: Pedro
# 


import wnck, gtk
from collections import deque
import time
import keybinder
import configuration



maximized_window_geometry = gtk.gdk.get_default_root_window().property_get('_NET_WORKAREA')[2][:4]
upper_corner = maximized_window_geometry[:2]
screen_width = maximized_window_geometry[2]
screen_height = maximized_window_geometry[3]

#because window resizing is not acurate we need a quick dirty workaround
window_geometry_error_margin=30

#variable to hold the amount of windows since the last arrangement
arrangement_size = 0


def get_all_windows():
	def f_normal_window(window):
		if window.get_window_type() == wnck.WindowType.__enum_values__[0]:
			return True
		return False

	s = wnck.screen_get_default()
	while gtk.events_pending(): gtk.main_iteration()
	windows = s.get_windows_stacked()
	filtered_windows = filter(f_normal_window,windows)
	filtered_windows.reverse()
	return filtered_windows


def parse_simple_math_expressions(expression):
	expression = str(expression)
	expression = expression.replace('w',str(screen_width))
	expression = expression.replace('h',str(screen_height))
	return eval(expression)



def parse_geometry(geometry):
	return map(parse_simple_math_expressions,geometry)



def parse_arrangement(arrangement):
	return map(parse_geometry, arrangement)



def resize_windows(arrangement):
	global arrangement_size
	arrangement_numeric = parse_arrangement(arrangement)
	#print arrangement_numeric
	filtered_windows = get_all_windows()
	amount_of_windows = len(filtered_windows) 	
	
	if amount_of_windows < len(arrangement_numeric):
		arrangement_numeric = arrangement_numeric[:amount_of_windows]
  
	i = 0
	arrangement_size = len(arrangement_numeric) #global scope variable, also used to rotate windows
	while i < arrangement_size:
		geometry_list_args = [0,255]
		index = arrangement_size - (i+1) #we must start in the end in order to keep window order correct
		geometry_list_args.extend(map (int,arrangement_numeric[index]))
		filtered_windows[index].unmaximize()
		filtered_windows[index].set_geometry(*geometry_list_args)
		i+=1



def resize_single_window(geometries):

	def similar_geometries(ga,gb):
		for i in range(4):
			if abs(ga[i] - gb[i]) >= window_geometry_error_margin:
				return False
		return True
 
	window = wnck.screen_get_default().get_active_window()	
	window_original_geometry = window.get_geometry()

	#not an arrangement, but a list of geometires for that matter
	geometries_numeric = parse_arrangement(geometries)
	geometry_list_args = [0,255]
	
	i=1
	geometry_to_use_index=0	
	for geometry_numeric in geometries_numeric:
		if similar_geometries(geometry_numeric, window_original_geometry):
			geometry_to_use_index = i % len(geometries_numeric)
			break
		i+=1 

	geometry_list_args.extend(map (int,geometries_numeric[geometry_to_use_index]))
	window.unmaximize()
	window.set_geometry(*geometry_list_args)




def rotate_windows(dummy):
	global arrangement_size
	windows = get_all_windows()
	amount_of_windows = len(windows)
	
	if amount_of_windows > arrangement_size:
		windows = windows[:arrangement_size]
		
	geos = []
	for window in windows:
		window_geo = window.get_geometry()
		window_geo = window_geo[:4]
		geos.append(window_geo)
		
	#do the actual rotations, lets use deque as it's dramatically more efficient than a trivial shift implementation
  	windows_deq = deque(windows)
  	windows_deq.rotate(1)
  	
	rotation_len = len(windows_deq)
	i = 0
	while i < rotation_len:
		geometry_list_args = [0,255]
		index = rotation_len - (i+1) #again, start by the tail
		geometry_list_args.extend(map (int,geos[index]))
		windows_deq[index].unmaximize()
		windows_deq[index].set_geometry(*geometry_list_args)
		i+=1
	
	#(windows_deq[0]).activate(int(time.time())) #not sure why it doesn't work. if uncommented causes other windows beyond the rotated ones to hide behind current ones even after pressing ctrl+tab


callable_actions = dict(\
	resize_single_window=resize_single_window, \
	resize_windows=resize_windows, \
	rotate_windows=resize_windows \
)


def dispatcher(dis_param):
	func = dis_param[0]
	param = dis_param[1]
	wnck.screen_get_default().force_update() #doesn't apear to do much
	func(param)	
	
	
def run():	
	for action in configuration.conf_data:
		keybind = action['keybind']
		function_name = action['function']
		print function_name
		function = callable_actions[function_name]
		parameters = action['parameters']
		dispacher_parameters = [function, parameters]
		keybinder.bind(keybind, dispatcher ,dispacher_parameters)		

	gtk.main()
