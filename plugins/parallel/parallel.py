#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

import os.path
import threading
from libopensesame import sequence
from libqtopensesame.items import sequence as qtsequence
from libqtopensesame.items import qtplugin

class parallel_process(threading.Thread):

	"""A wrapper for a single process"""
	
	def __init__(self, item):
	
		"""
		Constructor
		
		Arguments:
		item -- the item to run
		"""
	
		threading.Thread.__init__(self)
		self.item = item
		self.exception = None
	
	def run(self):	
	
		"""Runs the item"""
	
		try:
			self.item.run()
		except Exception as e:
			self.exception = e

class parallel(sequence.sequence):

	"""
	The parallel plug-in behaves much like a sequence, but it runs items in
	parallel. The parallel exits when the last item is finished
	"""
	
	def run(self):
	
		"""
		Run the parallel
		
		Returns:
		True on success, False on failure
		"""
			
		# Optionally flush the responses to catch escape presses
		if self._keyboard != None:
			self._keyboard.flush()
			
		# Create a list of threads
		tl = []	
		for item, cond in self._items:		
			if eval(cond):				
				tl.append(parallel_process(self.experiment.items[item]))
				
		# Run all threads
		for t in tl:
			t.start()
			
		# Wait for the threads to finish
		while True:		
			alive = False		
			for t in tl:
				if t.is_alive():
					alive = True
				if t.exception != None:
					raise t.exception
			if alive:
				self.sleep(100)
			else:
				break
			
		return True	
	
class qtparallel(qtsequence.sequence, qtplugin.qtplugin):

	"""Parallel GUI"""

	def __init__(self, name, experiment, string=None):

		"""
		Constructor

		Arguments:
		name -- the name of the item
		experiment -- an instance of libopensesame.experiment

		Keyword arguments:
		string -- a string with the item definition (default=None)
		"""

		qtsequence.sequence.__init__(self, name, experiment, string)
		self.item_type = 'parallel'
		self.description = "Runs a number of items in parallel"		
		qtplugin.qtplugin.__init__(self, __file__)
		

